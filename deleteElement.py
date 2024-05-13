def deletElement(array,index):
    if index > len(array)-1 or index < 0:
        print("Invalid index")
        return array
    array.pop(index)
    return array

# test
array=[3,7,1,9,4]
print(deletElement(array,10))
