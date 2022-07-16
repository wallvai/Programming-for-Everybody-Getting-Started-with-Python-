score = input("Enter Score: ")
score_float = float(score)
if 1 >= score_float >= 0 :
    if score_float >= 0.9 :
        print("A")
    elif score_float >= 0.8 :
        print("B")
    elif score_float >= 0.7 :
        print("C")
    elif score_float >= 0.6 :
        print("D")
    elif score_float < 0.6 :
        print("F")
    else :
        print("There is a problem with the input, please retype again.")
else :
    print("Enter a proper value.")
