name = "Alvin"
#list or array
classNames = ["joan","gilbert","emma","hun"]
#data type
print(type(classNames))
#list of floats
courseworknames= [1,45,76,34]\

#checking the size of a list
print(len(courseworknames))

#appending(adding elements)
classNames.append("paul")
print("size after appending",len(classNames))
#removing
classNames.remove("joan")

print(classNames[0])
#reading values from a list or errays
for range in classNames:
    print(range)
#while loop
i = 6
while i < len(classNames):
    print(classNames[i])

#list of districts
districts=["masaka","ibanda","wakiso","mukono","gulu","arua","entebbe","kitgum","napak","nakasongola","luwero"]
#data type
print(type(districts))
#adding districts
districts.append("kamwenjje")
districts.append("rwatura")
districts.append("Sheema")
#size
print(len(districts))
#display elements
for d in districts:
    print(d)
#Remove
districts.remove("masaka")
print(districts)
#count
districts=["masaka","ibanda","wakiso","mukono","gulu","arua","entebbe","kitgum","napak","nakasongola","luwero"]
for index, item in enumerate(districts):
    print(index, item)
