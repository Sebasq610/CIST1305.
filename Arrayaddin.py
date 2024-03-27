def sequential_search(array, target):
    for i in range(len(array)):
        if array[i]==target:
            return i
        
    return -15

array=[]
a=1    
while a <= 100:
    array.append(a)
    a=a+1
print(array)
target=int(input("What is your target value? "))

index=sequential_search(array,target)

if index != -1:
    print("The target value was found at index", index)
else:
    print("The target value was not found in the array")

sequential_search(array, target)
