def swapText():  
    file1n = input("Which file would you like to open first?")
    file2n = input("Which file would you like to open second?")
    with open(file1n,'r') as a:
        data_a = a.read()
    with open(file2n,'r') as b:
        data_b = b.read()
    with open(file1n,'w') as a:
        a.write(data_b)
    with open(file2n,'w') as b:
       b.write(data_a)

swapText()