#replaces any blank spaces in a input with '...'

string = input("Enter any input: ").split()
for i in range(len(string)):
    if i < len(string)-1:
        print(string[i] + "...", end  = "")
    else:
        print(string[i])
