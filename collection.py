
def calculate_discount(cost):       
    print("you are in discount part")
    if cost >100:
        return cost*0.8
    elif cost >=50:
        return cost*0.9
    else:
        return cost
cost=float(input("enter the cost"))
print(f"calculate_discount(cost))")

def kilometers_converter(kilomrters):
    print("you are in kilometers part")
    kilometers=float(input("enter kilometers"))
    miles=kilometers*0.621371
print(f"{kilometers}km={miles :.2f}")

def temperature_converter(temperature):
    print("you are in temperature part")
temp_c=float(input("enter your temperature"))
temp_k=(temp_c*9/5)+32
print(f"{temp_c}c={temp_k:.1f}kelvin")

def main():
    print("menu")
    print("press 1 for cost")
    print("press 2 for kolometers")
    print("press 3 for temperature")

def choices(choice):
    choice=float(input("enter your coice:"))
 
    if choice=="1":
    # calculate_discount(cost) elif choice=="2":
    elif choice=="2"
    # kilometers_converter(kilometers)
elif choice==(3)
    temperature_converter()
else:
    print("invalid choice please try again.")