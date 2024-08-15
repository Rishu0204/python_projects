import csv
import os
from bs4 import BeautifulSoup
import requests
import time
import datetime

def check():
    URLS = [
        'https://www.amazon.in/gp/aw/d/B0CQPHMWR3/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=6bab680f4c0692148df06644404f2dfd&hsa_cr_id=0&sr=1-3-undefined&ref_=sbx_be_dp_arbies_lsi4d_asin_2_bkgd&pd_rd_w=d4EdV&content-id=amzn1.sym.8b13584a-c7fa-402c-b0a3-ddf39b989f1f&pf_rd_p=8b13584a-c7fa-402c-b0a3-ddf39b989f1f&pf_rd_r=KD2AKQR2ZX1N6B2TE1WV&pd_rd_wg=rmw2y&pd_rd_r=ffc4158e-a65d-4ca2-a2dc-2b8b85e4e762&th=1',
        'https://www.amazon.in/gp/aw/d/B0CW3H8YKD/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=250db33181732dc212a7561c2574bbd3&hsa_cr_id=0&sr=1-2-undefined&ref_=sbx_be_dp_arbies_lsi4d_asin_1_title&pd_rd_w=5cHpp&content-id=amzn1.sym.8b13584a-c7fa-402c-b0a3-ddf39b989f1f&pf_rd_p=8b13584a-c7fa-402c-b0a3-ddf39b989f1f&pf_rd_r=17BPXGHY5VK8EBBP1Y69&pd_rd_wg=Lp2x0&pd_rd_r=e6daee4a-5d9a-4512-8ecf-794244926e4d'
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/"
    }

    products = {}

    for URL in URLS:
        try:
            # Request the page
            page = requests.get(URL, headers=headers)
            page.raise_for_status()
            print(page)  # Check for HTTP errors
        except requests.RequestException as e:
            print(f"Error fetching the URL {URL}: {e}")
            continue
        
        try:
            # Parse the page content
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Extract title
            title = soup.find(id='titleSection').get_text().strip()
            
            # Extract price section
            price = soup.find(id='corePriceDisplay_desktop_feature_div').get_text()
            
            # Extract the actual price
            actual_price = price.split('₹')[1].split()[0].replace(',', '')
            
            # Extract the discount percentage
            discount = None
            if '-%' in price:
                discount = price.split('-')[1].split('%')[0].strip() + '%'
            elif '%' in price:
                discount = price.split('%')[0].split()[-1].strip() + '%'
            if discount:
                discount = discount[1:]
            
            # Get the current date
            date = datetime.date.today()
            
            # Store the product details in the dictionary
            products[title] = [actual_price, discount, date]
        except Exception as e:
            print(f"Error processing the URL {URL}: {e}")

    # Define the file path
    file_path = 'AmazonwebScraperData.csv'
    
    # Check if the file exists and write data accordingly
    file_exists = os.path.isfile(file_path)
    
    try:
        with open(file_path, 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            
            # Write the header only if the file does not exist
            if not file_exists:
                header = ['Title', 'Price', 'Discount', 'Date']
                writer.writerow(header)
            
            # Write each product's data
            for title, details in products.items():
                writer.writerow([title, details[0], details[1], details[2]])
    except IOError as e:
        print(f"Error writing to the CSV file: {e}")

# Run the check function every 24 hours
while True:
    check()
    time.sleep(86400)  # Sleep for 24 hours
