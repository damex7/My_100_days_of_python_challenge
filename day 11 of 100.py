x = int(input("input a number for x: " ))
y = int(input("input a number for y: " ))
z = int(input("input a number for z: " ))

print(x,y,z)

if x<y and x<z:
    print("y is the lowest number")
elif x>y and x>z:
    print ("x is the highest number")
if y<x and y<z:
    print("y is the lowest number")
elif y>x and y>z:
    print ("y is the highest number")
if z<x and z<y:
    print("z is the lowest number")
elif z>x and z>y:
    print ("z is the highest number")