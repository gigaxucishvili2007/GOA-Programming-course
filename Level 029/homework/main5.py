'''5) შექმენი ფუნქცნია lion5() სადაც მომხმარებელს შეეკითხებით სანამ პაროლს არ გამოიცნობს მანამდე დაუწეროს "პაროლი არასოწორია" მინიშნება while loop ი გამოიყენეთ'''

# def lion5():
    # x = input("Enter a password")
    # while x != "gigaxuco":
        # return "პაროლი არასწორია"
    # return "სწორია პაროლი"
# print(lion5())


def lion5(): # create a function
    password = input("Enter a password") # required password
    while password != "giga": # while password is not "giga"
        password = input("Enter a password") # ( infinite loop )
    return "your password is correct" # else:
print(lion5()) # calling a function