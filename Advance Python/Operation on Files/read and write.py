s = open("file.txt", "a")
s.write("This is a file2\n")
s.close()
read_file = open("file.txt").read()
print (read_file)