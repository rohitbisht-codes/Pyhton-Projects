



while True:
    print("1.ADD")
    print("2.SUB")
    print("3.DIVIDE")
    print("4.multiply")
    print("5.Exit")
    choice = int(input("enter your choice : "))

    if choice == 5:
            break

    elif choice in (1,2,3,4):
         m = float(input("Enter your first number: "))
         n = float(input("enter your seconf number: "))


         if choice == 1:
             print(f"addition is {m+n}")
             
            
         elif choice == 2:
            print(f"subbtraion is{m-n}")
            
         elif choice == 3:
            print(f"division is {m/n}")
            
         elif choice == 4:
            print(f"multiplication is {m*n}")
            
        
         
           
           
    
        
        