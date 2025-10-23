## Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt


for i in range(26):
    letter = chr(65 + i)
    filename = letter + ".txt"
    file = open(filename,"w")
    file.write("This is file " + filename)
    file.close()
    