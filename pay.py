hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter the rate: ")
frate = float(rate)
if h <= 40:
    pay = frate * h 
else:
    pay = (1.5 * frate)* (h - 40) + (40 * frate)
print(pay)