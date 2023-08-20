while True:
  try:
    choice = int(input("Choose the following way for mathematics:\n1 For Arithmetic Operations\n2 For Trigonometric Operations\n3 Exit\nWaiting for input -----> "))
    if choice not in [1,2,3]:
      print("\nEnter the number from the series otherwise no output will be displayed\n")
      continue
    # else:
    #   break
  except:
    print("\nEnter the number from the series otherwise no output will be displayed\n")
    continue
  
  if choice == 3:
    break
  while True:
    if choice == 1:
      try:
        option = int(input("\n1 For Addition\n2 For Subtraction\n3 For Multiplication\n4 For Divison\n5 For Exit Arithmetic Opertaions\nWaiting for input -----> "))
        if option not in [1,2,3,4,5]:
          print("\nEnter the number from the series otherwise no output will be displayed\n")
          continue
      except:
        print("\nEnter the number from the series otherwise no output will be displayed22221\n")
        continue

      if option == 1:
        added = []
        i = 0
        while True:
          try:
            if i == 0:
              num1 = int(input(f"Enter the number {i+1}: "))
              added.insert(i,num1)
              i+=1
            elif i ==1:
              num2 = int(input(f"Enter the number {i+1}: "))
              added.insert(i,num2)
              i+=1
            if i <=1:
              continue
          except:
            print("\n ERROR:Please enter integer")
            continue
          print("\n======================================================================================")
          print(f"Result is : {sum(added)}")
          print("======================================================================================\n")
          break

      elif option == 2:
        i=0
        while True:
          try:
            if i == 0:
              num1 = int(input(f"Enter the number {i+1}: "))
              i+=1
            elif i ==1:
              num2 = int(input(f"Enter the number {i+1}: "))
              i+=1
            if i <=1:
              continue
          except:
            print("\n ERROR:Please enter integer")
            continue
          print("\n======================================================================================")
          print(f"Result is : {num1 - num2}")
          print("======================================================================================\n")
          break

      elif option == 3:
        i=0
        while True:
          try:
            if i == 0:
              num1 = int(input(f"Enter the number {i+1}: "))
              i+=1
            elif i ==1:
              num2 = int(input(f"Enter the number {i+1}: "))
              i+=1
            if i <=1:
              continue
          except:
            print("\n ERROR:Please enter integer")
            continue
          print("\n======================================================================================")
          print(f"Result is : {num1*num2}")
          print("======================================================================================\n")
          break
      elif option == 4:
        i=0
        while True:
          try:
            if i == 0:
              num1 = int(input(f"Enter the number {i+1}: "))
              i+=1
            elif i ==1:
              num2 = int(input(f"Enter the number {i+1}: "))
              if num2 == 0:
                continue
              i+=1
            if i <=1:
              continue
          except:
            print("\n ERROR:Please enter integer")
            continue
          print("\n======================================================================================")
          print(f"Result is : {num1/num2}")
          print("======================================================================================\n")
          break
      elif option == 5:
        break


    elif choice ==2:
      pass

  
