def sortAlphabets(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

array=["m","a","k","g","j"]
print(sortAlphabets(array))


