'''4) შექმენი ფუნქცნია lion4() სადაც შევქმნით ცარიელ მასივს და for loop ის გამოყენეით + .appnd() შევიტანთ მხოლოდ კენტ რიცხვებს'''

# def lion4(list):
#     for x in range(51):
#         if x % 2 != 0:
#             list.append(x)
# lion4()


def lion4(): # empty
    empty = [] # empty
    for y in range(21): # sequence numbers
        if y % 2 != 0: # check condition
            empty.append(y) # add
    return empty # last result show on screen
print(lion4()) # calling function