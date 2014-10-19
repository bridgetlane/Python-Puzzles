# tells you if a given string is a palindrome
def palindrome(string):
    for i in string:                        # remove non-alphabetical characters
        if (i.isalpha() == False):
            string = string.replace(i, "")
        if (i.isupper() == True):
            string = string.replace(i, i.lower())
    reverse = ""                            # create the reverse string
    i = len(string) - 1
    while (i >= 0):
        reverse += string[i]
        i -= 1
    
    is_pal = False
    if ((len(string) > 1) and (string == reverse)):
        is_pal = True
    
    return is_pal
   
# some examples   
def main():
    print(palindrome("Taco cat"))
    print(palindrome("not a palindrome :("))
    print(palindrome("Amor, Roma"))
    print(palindrome("A man, a plan, a canal: Panama"))
    print(palindrome(""))                   # is not fooled by empty strings/one letter

main()