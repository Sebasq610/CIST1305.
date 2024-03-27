#Sebastian Quesada Barona
#3/26/2024
#Bubble sort algorithm for sorting golf scores

def bubble():
    max=len(scores)
    for i in range(max - 1):
        for n in range(0, max - i - 1):
            if scores[n] > scores[n+1]:
                scores[n], scores[n+1]=scores[n+1], scores[n]

scores=[]
for i in range(10):
    score = int(input(f"Enter golf score{i+1}:" ))
    scores.append(score)

bubble()

print("sorted golf scores in asending order: ")
for score in scores:
    print(score)
