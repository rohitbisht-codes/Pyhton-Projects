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
def armstong():
   n = int(input("Enter Number: "))
   last =0
   total=0
   original = n
   while(n!=0):
      last = n% 10
      total =total+last**3
      n = n//10
   if(total == original):
      print("It is armstrong number")
   else:
      print("It is not armstong number")     
def reverse():
   n = int(input("Enter number: "))
   last = 0
   reverse =0
   while(n!=0):
      last = n%10
      reverse = reverse*10+last
      n = n//10
   print(reverse)
def count_digit():
   n = int(input("Enter Inout: "))
   count = 0
   last = 0
   while(n!=0):
      last = n%10
      count = count+1
      n = n//10
   print(count)
def Sum_of_Digits():
   n = int(input("Enter inout: "))
   total = 0
   last = 0
   while(n!=0):
      last =  n%10
      total = total + last
      n = n//10
   print(total)
def Largest_Digit():
   n = int(input("Enter numbers: "))
   largest = 0
   while(n!=0):
      last = n%10
      if(last>largest):
         largest = last;
      n = n // 10
   print(largest)
def Smallest_Digit():
   n = int(input("Enter numbers: "))
   smallest = 9
   while(n!=0):
      last = n%10
      if(last<smallest):
         smallest = last;
      n = n // 10
   print(smallest)
def even_odd():
   n = int(input("Enter input: "))
  

   if(n%2==0):
         print("Even nuber")
   else:
         print("Odd number")
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
    elif(choice == 2):
     result = primecheck()
     print(result)
    elif(choice==3):
       result = palindrome()
       print(result)
    elif(choice ==4):
       result = armstong()
       print(result)
    elif(choice == 5):
       result = reverse()
       print(result)
    elif(choice == 6):
       result = count_digit()
       print(result)
    elif(choice == 7):
       result = Sum_of_Digits()
       print(result)
    elif(choice == 8):
       result = Largest_Digit()
       print(result)
    elif(choice == 9):
       result = Smallest_Digit()
       print(result)
    elif(choice == 10):
       result = even_odd()
       print(result)