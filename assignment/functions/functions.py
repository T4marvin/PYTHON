def average(num1,num2,num3):
    sum=num1+num2+num3
    avg= sum/3
    print(avg)
    return avg,sum

average,sum(100,90,92)

def calculate_area(length,width):
    area= length*width
    return area
rectangle_area = calculate_area
print(f"The area of the rectangle is :{rectangle_area}")