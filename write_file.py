
def write_file(self, content, filename):

    with open(filename, 'w') as file:
        file.writelines(content)
