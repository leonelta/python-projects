from sys import argv

script, filename = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)