def multiply(num,num2):
    return num * num2
#invoke the function
result=multiply(100,20)
print(f"the multiplication of 100 and 20 is:{result}")


#BMI Calculator function
def calculator_bmi(weight,height):
    bmi=weight/height**2
    return round (bmi,2)
    #user input
    weight=float(input("enter your weight in kg:"))
    height=float(input("enter your height in metres:"))
    # invoke the function
result=calculate_bmi(w,h)
print(f"your BMI is:{result}")

# program to check age 
def check_age(age):
    ifage< 18:
        return "you are a minor."
    return"you are an alduld."
user_age= int(input("entrer your age:"))
# invoke the function
result_age=check age(user_age)
print(result_age)


