a =float(input()) 
b =float(input())
c =float(input())
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + (d)**0.5) / (2*a)
    root2 = (-b - (d)**0.5) / (2*a)
    print("The roots are real and different.")
    print("Root 1 = ",root1)
    print("Root 2 = ",root1)
elif d == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root = ",root)
else:
    real_part = -b / (2*a)
    imaginary_part = ((-d)**0.5) / (2*a)
    print("The roots are complex (imaginary).")
    print("Root 1 = ",real_part,", + ",imaginary_part," i")
    print("Root 1 = ",real_part,", - ",imaginary_part," i")