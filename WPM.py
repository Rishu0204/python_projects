import time

def wpm_calculator():
    phrase="hello my name is billy butcher"

    word_count=len(phrase.split())
    begin=input('Please type: '+ phrase+"\n"+'enter when ready.')
    
    t0=time.time()
    attempt=input('\n')
    t1=time.time()
    attempt_time=(t0-t1)/60
    wpm=str(round(word_count/attempt_time,2))

    if attempt==phrase:
        print('\n'+'your wpm: '+wpm)
    else:
        print('\n'+'Typed incorrectly. Please try again.')
wpm_calculator()

while True:
    try_again=input("Do you want to try again (Y/N): ")

    if try_again.lower()=='y':
        wpm_calculator()
    else:
        break
    

    