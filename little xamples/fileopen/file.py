from sys import argv

file, filet = argv

txt = open(filet.txt)

print(f"Here's your file {filet}:")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
