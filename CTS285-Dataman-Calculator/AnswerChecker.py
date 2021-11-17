def ansChk():
    count = 0
    wrong = 0
    loop = True
    
    chkLoop = True
    operation = int(input("""
What operation do you want:
1. Add
2. Subtract
3. Multiply
4. Divide
"""))    
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    while loop == True:
        if operation == 1:    
            ans = int1 + int2
            
            print(int1," + ", int2)
        elif operation == 2:
            ans = int1 - int2
            
            print(int1," - ", int2)
        elif operation == 3:
            ans = int1 * int2
            
            print(int1," * ", int2)
        elif operation == 4:
            ans = int1 / int2
            
            print(int1," / ", int2)
        else:
            print("Error")
        
        while chkLoop == True:
            userAns = int(input("Enter the answer: "))
            if userAns == ans:
                print("You got it!")
                count += 1
                print("Winning Count:",count)
                ask = int(input("Do you want to continue?\n\
1. Yes\n\
2. No\n"))
                if ask ==  1:
                    ansChk()
                elif ask == 2:
                    return
                else:
                        print("Error")
                    
            
            elif userAns != ans:
                if wrong == 3:
                    print("The correct answer is:",ans)
                    ask = int(input("Do you want to continue?\n\
1. Yes\n\
2. No\n"))
                    if ask ==  1:
                        ansChk()
                    elif ask == 2:
                        return
                    else:
                        print("Error")
                    
                else:
                    print("Try again\n")
                    wrong += 1
                    ask = int(input("Do you want to continue?\n\
1. Yes\n\
2. No\n"))
                    if ask ==  1:
                        pass
                    elif ask == 2:
                        return
                    else:
                        print("Error")
                    
                
                
