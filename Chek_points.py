# to check points
def check_points(points):
    if points > 36: 
        return"fail." 
    else:
         return"pass."
  user_points=int(input("enter your points:"))
#invoke the function
result_points=check_points(user_points)
print(result_points)