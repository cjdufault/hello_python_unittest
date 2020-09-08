import re


sp_char_regex = re.compile("[!@#$؋ƒ₼៛¥₡₱£€¢﷼₪₩₭₨₮₦₽฿₴₫₿%^&*()<>?/\|}{~:\[\],.+-]")


def main():
    string = input("Type a sentence: ")
    
    # check if string will make a valid python variable name
    if not is_valid_variable(string):
        proceed = show_warning("Won't produce a valid variable name. Continue? Y/n: ")
        if not proceed:
            return
        
        # offer to strip out special characters, if there are any
        if contains_sp_char(string):
            strip_special_char_yn = show_warning("Would you like to remove special characters? Y/n: ")
        
            if strip_special_char_yn:
                string = strip_special_char(string)
        
    print(make_camel(string))
    
    
def make_camel(string):
    words = string.split()
    
    if len(words) > 0:
        # remove 1st word and use it in all lower case to start out our output string
        camel_string = words.pop(0).lower()
        
        # add all other words, capitalized, to output string
        for word in words:
            camel_string += word.title()
    else:
        camel_string = ""
        
    return camel_string
    
    
# returns True if a string is a valid python variable name, False if not
def is_valid_variable(string):
    # check that 1st char is valid
    if not string[0].isalpha() or string[0] == "_":
        return False
    
    return not contains_sp_char(string)


# returns True if string contains special characters
def contains_sp_char(string):
    # check for special characters, now w/ a stupid number of currency symbols
    if sp_char_regex.search(string) == None:
        return False
    return True
    

# shows a warning, returns True if user wants to continue, False if not
def show_warning(string):
    answer = input(string)
    if answer.lower() == "y" or answer.lower() == "yes":
        return True
    elif answer.lower() == "n" or answer.lower() == "no":
        return False
    else:
        return show_warning(string) # ask again if answer is other than yes or no
    

# removes any characters found in sp_char_regex
def strip_special_char(string):
    return re.sub(sp_char_regex, "", string)


if __name__ == "__main__":
    main()
