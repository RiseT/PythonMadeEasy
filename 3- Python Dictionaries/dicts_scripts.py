##dict1 = {1:1, 2:2, 3:3, 4:4, 5:5}
##count = 0
##
##for value in dict1.values():
##    count = count + value
##
##print(count)


# challenge take the following dict and print out
## only those words that end in vowels

##dict2 = {1: "music", 2: "pizza", 3: "eggs", 4: "opera", 5: "menu"}
##vowels= ["a", "e", "i", "o", "u"]
##for v in dict2.values():
##    if v[-1] in (vowels):
##        print(v)
##    else:
##        pass

# Challenge: take the following dict of 4 mappings
# and  if upper add my_list, if lower, lower_list

dict1 = {1: "ONE", 2: "two", 3: "THREE", 4: "four"}
upper_list = []
lower_list = []

for k, v in dict1.items():
    if dict1[k].isupper():
        upper_list.append(v)
    else:
        lower_list.append(v)
print(" These are the upper case words: ", upper_list)
print(" These are the lower case words", lower_list)
