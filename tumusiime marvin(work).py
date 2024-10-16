#NUMBER1
year_of_birth=int(input("Enter your year of birth: "))
current_year =2024
age= current_year-year_of_birth
print(f"You are{age}years old")
#NUMBER2
A=float(input("Enter number A:"))
B=float(input("Enter number B:"))

sum_result=A+B
product_result=A*B

print(f"sum of these is {sum_result}and product of these is{product_result}")
#NUMBER 3
N=float(input("Enter a number"))
square=N ** 2

print(F"Number is {N}")
print(f"Its square is{square}")
#NUMBER 4
#Read two numbers from the user
A=float(input("Enter Nnumber A:"))
B=float(input("Enter number"))
#calculate the sum and product
sum_a_b=A+B
prod_a_b=A*B
#print results
print(f"sum of {A}and {B} is{sum_a_b} ")
print(f"product of{A}and {B}is{prod_a_b}")
#NUMBER 5
#calculate area of the resctangle
length=float(input("Enter the length"))
width=float(input("Enter the width"))
#calculate the perimeter and Area
area=length*width
perimeter=2*(length+width)
#print results
print(f"area of rectangle is={area}")
print(f"the perimeter of the rectangle is={perimeter}")
#NUMBER 6
#read celsius value(28)
Celsius=float(input("Enter the celsuis value"))
#convert to farenhiet using the formula
farenhiet_t=1.8*Celsius+32
#print the results
print(f"the farenhiet value is {farenhiet_t}")
#NUMBER 7
#radias
radius=float(input("What is the raduis?"))
#calculate the diameter and area
area_i=3.14*radius**2
diameter=radius*2
#print diameter and area
print(f"the diameter is {diameter}")
print(f"the area of the rectangle is {area_i}")

#NUMBER8
Base=float(input("Enter the base number of the triangle "))
height=float(input("Enter the height number of triangle"))
triangle_area = Base*height*0.5
print(f"The Area of triangle is{triangle_area}")
#NUMBER 9
Price=float(input("enter your price"))
vat_rate=0.14
vat_due=Price*vat_rate
price_with_vat=Price+vat_due
print(f"VAT due{vat_due}")
print(f"price with VAT:{price_with_vat}")
#number 10
side_a=float(input("Enter side A"))
side_b=float(input("Enter side b:"))
hypotenuse= (side_a,side_b)
print(f"hypotunese{hypotenuse}")
#NUMBER 11
cost_per_litre=1.50
intial_reading=float(input("Enter the intial water consumption(in kilolitres)"))
final_reading=float(input("Enter the final water consuption (in kilolitres):"))
consumption=final_reading*cost_per_litre
cost=consumption*cost_per_litre
print(f"consumption:{consumption}")
print(f"Cost:Shs{cost}")
#NUMBER 12
initual_km=float(input("Enter initual Km reading"))
final_km=float(input("Enter final reading:"))
fuel_litres=float(input("enter fuel used (in litres)"))
distance=final_km-initual_km
consumption_m=distance/fuel_litres
print(f"Distance:{distance}")
print(f"consumption is{consumption_m}")
#Number 13
current_population= 43_000_000
growth_rate=0.123
population_2025=current_population*(1+growth_rate)**1
population_2026=current_population*(1+growth_rate)**2
population_2027=current_population*(1+growth_rate)**3
print(f"2025 population:{population_2025}")
print(f"2026 population:{population_2026}")
print(f"2027 population :{population_2027}")