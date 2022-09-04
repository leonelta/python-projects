from sys import argv

script, filename = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_file(line_count, f):
    print(line_count, f.readline())