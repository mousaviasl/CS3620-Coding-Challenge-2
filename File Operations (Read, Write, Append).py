with open("demo.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a demo file.\n")


with open("demo.txt", "r") as file:
    content = file.read()
    print("File contents:\n", content)


with open("demo.txt", "a") as file:
    file.write("New line added to the file.\n")