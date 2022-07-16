list = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num = int(num)
        list.append(num)
    except :
        print("Invalid input")
        continue
largest = max(list)
smallest = min(list)
print("Maximum is", largest)
print("Minimum is", smallest)
