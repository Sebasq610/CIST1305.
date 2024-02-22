#This range program only works with intergers(int) not Real(float) numbers
def hours():
    hour= int(input("What is your hours? "))
    while hour not in range(0, 41):
        print("Invalid hours")
        hour= float(input("What is your hours? "))
    
    print("You worked", hour,"hours.")

hours()