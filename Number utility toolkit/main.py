def factorial():
    a = int(input("Enter number: "))
    fact = 1
    for i in range(1,a+1):
       fact = fact*i
    return fact
def primecheck():
   a = int(input("Enter number: "))
   found = 0
   for i in range(2,a):
      if (a%i==0):
         found =1
         break
   if(found == 1):
      print("It is notprime")
   else:
      print("It is  prime")  
def palindrome():
   n = int(input("Enter Number: "))
   last =0
   revrse = 0
   original = n
   while(n!=0):
      last = n % 10
      revrse = revrse*10+last
      n = n//10  
   if(revrse == original):
      print("It is palindrome")
   else:
      print("It is not Palinrome")     
                      
print("========== NUMBER UTILITY TOOLKIT ==========")
print("1. Factorial")
print("2. Prime Check")
print("3. Palindrome")
print("4. Armstrong")
print("5. Reverse number")
print("6. Count Digit")
print("7. Sum of digit")
print("8. Largest Digit")
print("9. Smallest Digit")
print("10. Even/Odd")
print("11. Exit")
choice = int(input("Enter Your Choice: "))

if(choice == 11):
    print("Thank you for using Number Utility Toolkit")
else:
    if(choice == 1):
     result =factorial()
     print(result)
    if(choice == 2):
     result = primecheck()
     print(result)
    if(choice==3):
       result = palindrome()
       print(result)
