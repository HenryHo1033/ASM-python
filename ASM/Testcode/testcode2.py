def main():

    infile = open('test.txt', 'r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)
main()