'''4) შექმენი ფუნქცნია lion4() სადაც შევქმნით ცარიელ მასივს და for loop ის გამოყენეით + .appnd() შევიტანთ მხოლოდ კენტ რიცხვებს'''

def lion4(arr1):
    # function
    for x in range(1,10,2):
        # iteration for numbers
        arr1.append(arr1)
        # add value in end list
# calling a function
print(lion4([]))