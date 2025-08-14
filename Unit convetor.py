# converting kilometers
def kilometers_converter(kilometers)
kilometers=400
miles=kilometers*0.621371
print(f"{kilometers}km={miles:.2f} miles")

temp_c =200
temp_k =(temp_c*9/5)+32
print(f"{temp_c}c={temp_k:.1f}kelvin")

kilometres=float(input("enter kilometers"))
miles=kilometers*0.621371
print(f"{kilometers}km={miles:.2f}")

temp_c=float(input("enter your temerature"))
temp_k=(temp_c*9/5)+32
print(f"{temp_c}c={temp_k:.1f}kelvin")
