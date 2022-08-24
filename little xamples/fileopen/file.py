from sys import argv

file, filet = argv

txt = open(filet)

print(f"Here's your file {filet}:")
print(txt.read())