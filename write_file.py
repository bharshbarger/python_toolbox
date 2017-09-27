import sys

def write_file(self, content, filename):
    try:
        with open(filename, 'w') as file:
            file.writelines(content)
            file.close()
    except Exception as e:
        print(e)
        sys.exit(1)
