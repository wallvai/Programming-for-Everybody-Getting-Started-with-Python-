hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs_float = float(hrs)
    rate_float = float(rate)
except:
    print("\nPlease enter a numeric input.")
    quit()
if hrs_float > 40 :
    result = (hrs_float-40)*(rate_float*1.5)+(40*rate_float)
else :
    result = hrs_float*rate_float
print("\nResult:", result)
