
# searching function
def search(array,number):
    for j in array:
        if j == int(user_input2):
            print("yes, the number exists " , array.count(int(user_input2)),"times")
            return
    print("The number doesn't exist")

# take user input
user_input=input("Enter your numbers by separating them with space: ")
temp_array=user_input.split(" ")
array=[]
for i in temp_array:
    array.append(int(i))
#take  the number to be searched
user_input2=input("Search a number: ")
search(array,user_input2)


#merege sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted(left, right)

# a fucntion that merges the subdivided arrays
def merge_two_sorted(list1, list2):
    list3 = []
    a = len(list1)
    b = len(list2)
    i = j = 0
    while i < a and j < b:
        if list1[i] <= list2[j]:
            list3.append(list1[i])
            i += 1

        else:
            list3.append(list2[j])
            j += 1

    while i < a:
        list3.append(list1[i])
        i += 1
    while j < b:
        list3.append(list2[j])
        j += 1
    return list3

#asking the user if want to sort
user_input3=input("want to sort? (y/n): ")
if user_input3 == "y":
    print(merge_sort(array))
