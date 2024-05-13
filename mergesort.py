# a function that divides the array into the sub arrays
def merge_sort(array):
    if len(array) <= 1:
        return array
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
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

array=[5,1,4,2,6,8,6]
print(merge_sort(array))