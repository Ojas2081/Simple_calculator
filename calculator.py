import math
from Modue.funcs import Arithmetic, Trigonometry
while True:
    try:
        print("\n*************************************\nPress any integer from the following\n*************************************")
        choice = int(input(
            "Choose the following way for mathematics:\n1 For Arithmetic Operations\n2 For Trigonometric Operations\n3 For Exit\nWaiting for input -----> "))
        if choice not in [1, 2, 3]:
            print(
                "\nEnter the number from the series otherwise no output will be displayed\n")
            continue
        # else:
        #   break
    except:
        print("\n ERROR:Enter the number from the series otherwise no output will be displayed\n")
        continue

    if choice == 3:
        break
    while True:
        if choice == 1:
            try:
                option = int(input(
                    "\n1 For Addition\n2 For Subtraction\n3 For Multiplication\n4 For Divison\n5 For Exit Arithmetic Opertaions\nWaiting for input -----> "))
                if option not in [1, 2, 3, 4, 5]:
                    print(
                        "\nEnter the number from the series otherwise no output will be displayed\n")
                    continue
            except:
                print(
                    "\nEnter the number from the series otherwise no output will be displayed\n")
                continue

            if option == 1:
                added = []
                i = 0
                while True:
                    try:
                        if i == 0:
                            num1 = int(input(f"Enter the number {i+1}: "))
                            added.insert(i, num1)
                            i += 1
                        elif i == 1:
                            num2 = int(input(f"Enter the number {i+1}: "))
                            added.insert(i, num2)
                            obj = Arithmetic(num1, num2)
                            i += 1
                        if i <= 1:
                            continue
                    except:
                        print("\n*****ERROR:Please enter integer*****")
                        continue

                    result = obj.add()
                    break

            elif option == 2:
                i = 0
                while True:
                    try:
                        if i == 0:
                            num1 = int(input(f"Enter the number {i+1}: "))
                            i += 1
                        elif i == 1:
                            num2 = int(input(f"Enter the number {i+1}: "))
                            obj = Arithmetic(num1, num2)
                            i += 1
                        if i <= 1:
                            continue
                    except:
                        print("\n*****ERROR:Please enter integer*****")
                        continue

                    result = obj.subtract()
                    break

            elif option == 3:
                i = 0
                while True:
                    try:
                        if i == 0:
                            num1 = int(input(f"Enter the number {i+1}: "))
                            i += 1
                        elif i == 1:
                            num2 = int(input(f"Enter the number {i+1}: "))
                            obj = Arithmetic(num1, num2)
                            i += 1
                        if i <= 1:
                            continue
                    except:
                        print("\n*****ERROR:Please enter integer*****")
                        continue

                    result = obj.multiply()
                    break
            elif option == 4:
                i = 0
                while True:
                    try:
                        if i == 0:
                            num1 = int(input(f"Enter the number {i+1}: "))
                            i += 1
                        elif i == 1:
                            num2 = int(input(f"Enter the number {i+1}: "))
                            if num2 == 0:
                                print("\n******************************")
                                print("Error: Divisor cannot be Zero")
                                print("******************************")
                                continue
                            obj = Arithmetic(num1, num2)
                            i += 1
                        if i <= 1:
                            continue
                    except:
                        print("\n*****ERROR:Please enter integer*****")
                        continue

                    result = obj.divide()
                    break
            elif option == 5:
                break
            print(
                "\n======================================================================================")
            print(f"Result is : {result}")
            print(
                "======================================================================================\n")

        elif choice == 2:
            trig = ["sin", "cos", "tan", "cot", "sec", "cosec"]
            while True:
                print(
                    "1 For Sin\n2 For Cos\n3 For Tan\n4 For Cot\n5 For Sec\n6 For Cosec\n7 For Exit")
                try:
                    option = int(input(
                        "Enter the serial number of trigonometric function you want to choose: "))

                    if option not in [1, 2, 3, 4, 5, 6, 7]:
                        print(
                            "\nEnter the number from the series otherwise no output will be displayed\n")
                        continue
                    else:
                        break
                except:
                    print(
                        "\nEnter the number from the series otherwise no output will be displayed\n")
                    continue
            if option == 7:
                break

            while True:
                print("Enter the angle in radians or Degree")
                try:
                    angle_info = int(
                        input("Enter :\n\"1 For degree\" \n\"2 For radian\" \nWaiting for input -----> "))
                except:
                    print("\n*****ERROR: Enter proper integer value*****")
                    continue
                if angle_info not in [1, 2]:
                    print("\n*****Please Enter the value mentioned above*****")
                    continue
                else:
                    break

            while True:
                if angle_info == 1:
                    try:
                        angle = int(input("Enter the angle in Degree: "))
                        temp_angle = angle
                        angle = math.radians(angle)
                        obj = Trigonometry(angle)
                        break
                    except:
                        print("*****ERROR:Enter integer value for angle*****")
                        continue
                elif angle_info == 2:
                    try:
                        angle = float(input("Enter the angle in Radian: "))
                        temp_angle = angle
                        obj = Trigonometry(angle)
                        break
                    except:
                        print("*****ERROR:Enter integer value for angle*****")
                        continue

            if option == 1:
                result = obj.sin_trig()

            elif option == 2:
                result = obj.cos_trig

            elif option == 3:
                result = obj.tan_trig()

            elif option == 4:
                result = obj.cot_trig()

            elif option == 5:
                result = obj.sec_trig()

            elif option == 6:
                result = obj.cosec_trig()

            print(
                "\n======================================================================================")
            if angle_info == 1:
                print(f"Result for {trig[option-1]}({temp_angle}) : {result}")
            elif angle_info == 2:
                print(
                    f"Result(radians) for {trig[option-1]}({temp_angle}) : {result}")
            print(
                "======================================================================================\n")
