#Defining a program()
def calculateareaofrectangle():
    length = 4
    width = 5

    area = length*width
    print("Area is",area)
#RETURN FUNCTION
def calculateareareturn():
    lengt_h=6
    widt_h = 5
    are_a = lengt_h*widt_h
    return are_a
#calling a function(void)
calculateareaofrectangle()
#calling return
print("the area is(returning)",calculateareareturn())
#exercice
def mynames():
    names=input("What is your name")
    print("My names are",names)

mynames()

def names():
    name = input("What is your name")
    return name
print("Your return name is",names())
#Parameters 
def calculateareaofrectangle2():

    lenth = int(input("Enter your lenght"))
    widht = int(input("Enter your width"))
    area = lenth*widht
    return area

    print("the area is",area)



