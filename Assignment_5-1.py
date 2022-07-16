"""bu yazılım rastgele girilen değerlerin toplamını, ortalamasını ve
girilen sayı adetlerini üretir. kendi hata ayıklama sistemi vardır."""
num = 0
sum = 0.0
while True:
    x = input("Enter data: ")
    if x == "done":
        print("\n -All done.")
        break
    try:
        x_int = int(x)
    except:
        print("Invalid input.")
        continue
    sum = sum + x_int
    num = num + 1
    avg = sum/num
print("Total value: {}".format(sum))
print("Entered numbers: {}".format(num))
print("Average value: {}".format(round(avg,3)))
