#This program works with Real(float) numbers 
def main():
    hour=hours()
    rate=rates()
    gross(rate, hour)

def hours():
    hour= float(input("What is your hours? "))
    while hour < 0 or hour > 40:
        print("Invalid hours")
        hour= float(input("What is your hours? "))
    
    print("You worked", hour,"hours.")
    return hour

def rates():
    rate= float(input("What is your hourly rate? "))
    while rate < 7.5 or rate > 18.25:
        print("Invalid hourly rate")
        rate= float(input("What is your hourly rate? "))

    print("Your hourly rate is", rate)
    return rate

def gross(rate, hour):
    grossPay= rate * hour
    print("Your paycheck this week was", grossPay)

main()