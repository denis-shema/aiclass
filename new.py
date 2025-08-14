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

def calculate_discount():
    cost=float(input("enter the cost"))
    print("you are in discount part")
    if cost >100:
        final=cost*0.8
    elif cost >=50:
        final=cost*0.9
    else:
        final= cost

    print(f"discount cost:MK{final})")

def main():
    print("welcome to smart tools!")
    print("1.kilometers to miles converter")
    print("2.temperature convertor(c to k)")
    print("3.shop discount calculator")
    
    choice = input("choose an option(1-3):")
    if choice =="1":
            kilometers_convert()
    elif choice =="2":
             temperature_converter()
    elif choice =="3":
             calculate_discount()
    else:
        print("invalid choice please try again!")
main()