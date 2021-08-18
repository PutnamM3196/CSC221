loop = 1
storage = []
print("\nThis is the Double-a-number program")
user_int = int(input("Enter a number: "))
answer = user_int * 2
print(user_int,"doubled is:", answer)
storage.append(answer)
while loop == 1:
    menu = int(input("""
1. Enter another number
2. Display list of results
3. Exit\n\n"""))
    if menu == 1:
        user_int = int(input("Enter the number to double it: "))
        answer = user_int * 2
        storage.append(answer)
        print(user_int,"doubled is:", answer)
    elif menu == 2:
        print("Results:",storage)
    elif menu == 3:
        loop = 0
    else:
        print("Error, try again.")
print("\nResults:",storage)
print("Goodbye.")