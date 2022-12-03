# Python Program to Check if a String is a Pangram or Not
def checkPangramString(string):
    # creating a new string (alphabet string which stores all the alphabets of the english language
    AlphabetString = 'abcdefghijklmnopqrstuvwxyz'
    # Traverse through the alphabets string
    for char in AlphabetString:
        # Check if this character is present in given string .
        if char not in string.lower():
            # if yes then this character is not available hence return False
            return False
    # After the end of loop return True (which implies it is pangram)
    return True

    # given string
string = "hello their is fc road not zebra crossing just joking u mr nead which will find in pune very cheap shops quickly xerox centre not avaible "
# converting the given string into lower case
string = string.lower()
# passing this string to checkPangramString function which returns true
# if the given string is pangram else it will return false
if checkPangramString(string):
    print("The given string :", string, "--> is a pangram")
else:
    print("The given string", string, "is not a pangram")