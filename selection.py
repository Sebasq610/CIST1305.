#Sebastian Quesada Barona
#3/26/2024
#This program uses the selection sorting algorithm to sort names

def selection():
    max=len(names)
    for i in range(max - 1):
        min_idx = i
        for j in range(i + 1, max):
            if names[j] < names[min_idx]:
                min_idx=j
        names[i], names[min_idx]=names[min_idx], names[i]

names=[]
for i in range(20):
    name=input(f"Enter a name {i+1}: ")
    names.append(name)

selection()

print("Here are the names in Alphabetical order: ")
for name in names:
    print(name)
