def add_and_multiply(x, y, z):
    add_result = x + y 
    mult_result = add_result * z
    
    return mult_result

x = 10 
y = 20
z = 3

result1 = add_and_multiply(x=x,y=y,z=z)
print(f"Result 1 is {result1} for x = {x}, y = {y}, and z = {z}")

x2 = 5 
y2 = 15
z2 = 5

result2 = add_and_multiply(x=x2,y=y2,z=z2)
print(f"Result 2 is {result2} for x = {x2}, y = {y2}, and z = {z2}")