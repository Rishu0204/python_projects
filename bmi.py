height=float(input("Enter Your Height(in meters): "))
weight=float(input("Enter Your Weight(in Kg): "))

bmi=weight/(height*height)

if bmi<18.5:
    print("You Are Underweight")
elif bmi<24.9:
    print("You Are Normal")

elif bmi<29.9:
    print("You Are Overweight")
else:
    print("You Are Obese")