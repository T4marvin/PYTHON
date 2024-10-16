with open("tumix.docx","r") as f:
    content = f.read()
    print(content)


#APPEND
with open("tumix.txt","w")as f:
    f.write("Hello World\n")
    f.write("HeY MATTHEW\n")
