def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #input range
    if not 2<=len(s)<=6:
        return False
    #1st two characters not alphabets
    elif not s[0].isalpha() or s[1].isalpha():
        return False
    #checks for period, space and question mark
    elif "." or " " or "?" in s:
        return False
    #input not alphanumeric
    elif not s.isalnum():
        return False
    else:
        #no alphabet after first number
        for i in range(len(s)-1):
            if s[i].isdigit() and s[i+1].isalpha():
                return False
        #if all characters are number except 1st two, should print valid but not working
        if s[2:].isdigit():
            return True


main()
