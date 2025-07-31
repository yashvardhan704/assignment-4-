myfile="output.txt"
try:
    with open(myfile , "w") as file:
        file.write("this is a new line 1\n")
        file.write(" the is the second line\n")
        print(f" the content is added to new file named: {myfile}")
except FileNotFoundError:
    print(f"no file exist named: {myfile}")
try:
    with open(myfile, "r") as file:
        content=file.readlines()
        for i,line in enumerate(content):
            print(f"line{i+1}: {line.strip()}")
    print("the file content is succesfully created")
except FileNotFoundError:
    print(f"no file named {myfile} found")







