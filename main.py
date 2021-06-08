calculator = False
while not calculator:
    n1 = int(input("Give a number :"))
    n2 = int(input("Give the second number :"))

    while True:
        print("write 1 for addition")
        print("write 2 for subtraction")
        print("write 3 for multiplication")
        print("write 4 for division")
        calculating = input("Which operation do you want ? add/sub/mul/div ? :")

        c = ["1", "2", "3", "4", "5"]
        if calculating not in c:
            print("Unknown Operation . write the valid operation number which is defined.")
            continue

        # code for additional operation ----------------------
        if calculating == "1":
            ad = n1 + n2
            print('Your result is ', ad)
            break

        # code for Subtracting operation ---------------------------
        if calculating == "2":
            sb = n1 - n2
            print('Your result i s', sb)
            break

        # code for multiplication operation -------------
        if calculating == "3":
            ml = n1 * n2
            print("Your result is ", ml)

            break

        # code for divisional operation ---------------
        if calculating == "4":
            dv = n1 / n2
            print("Your result is ", dv)
            break
