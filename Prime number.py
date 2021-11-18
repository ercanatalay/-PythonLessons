number = int(input("Enter a number : "))
if number > 1:
   
   for i in range(2,number):
       if (number % i) == 0:
           print(number," It is not a prime number.")
           break
   else:
       print(number," It is a prime number.")
 
else:
   print(number," It is not a prime number.")