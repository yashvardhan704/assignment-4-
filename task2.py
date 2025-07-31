myfile="append.txt"
user_input=input("enter the data you want to store: ")
try:
    with open(myfile , "w") as file:
        file.write(f"{user_input}\n")

        print(f" the content is added to new file named: {myfile}")
except FileNotFoundError:
    print(f"no file exist named: {myfile}")
user_input2=input("enter the data you want to append: ")
try:
    with open(myfile, 'a') as file:
        file.write(f"{user_input2}\n")
        print("the content is succsesfully appended")
except FileNotFoundError:
    print("no file to be appended")

try:
    with open(myfile, "r") as file:
        content=file.readlines()
        for i,line in enumerate(content):
            print(f"line{i+1}: {line.strip()}")
    print("the file content is succesfully created")
except FileNotFoundError:
    print(f"no file named {myfile} found")


