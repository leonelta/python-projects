print("1) Create a new file")
print("2) Display th file")
print("2) Add a new subject to the file")

selection = int(input("Make a selection 1, 2 or 3: "))

if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("subject.txt", 'w')
    file.write(subject + "\n")
    file.close()
    
elif selection == 2:
    file = open("subject.txt", "r")
    print(file.read())
    
elif selection == 3:
    