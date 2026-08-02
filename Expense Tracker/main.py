print("========== EXPENSE TRACKER ==========")
print("1. Add Expense")
print("2. View All expense")
print("3. Search Expense")
print("4. Total Spending")
print("5. Exit")
choice = int(input("Enter your choice: "))
if(choice == 5):
    print("Thank You For Using Expense Tracker ")
else:
    if (choice == 1):
        n = input("Enter Expense: ")
        m = int(input("Enter ammount: "))
        with open ("expenses.txt","a")as f:
            f.write(n+","+str(m)+"\n")
            print("Expense added successfully!")
    elif (choice == 2):
        with open("expenses.txt","r") as f:
            data = f.read()
            print(data)
    elif(choice == 3):
        with open("expenses.txt","r") as f:
            data = f.read()
            n = input("Enter expenses to search: ")
            if n in data:
                print("Expenses Found")
            else:
                print("Not found")
    elif(choice == 4):
        with open("expenses.txt","r")as f:
          total = 0
          for i in f:
              data = i.split(",")
              total = total + int(data[1])
        print(total)



            




