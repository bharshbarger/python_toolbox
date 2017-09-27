import sys

def read_file(self, filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            return content
    except Exception as e:
        print(e)
        sys.exit(1)
