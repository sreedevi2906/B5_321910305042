Open In Colab
1.find minimum among the three numbers.

In [1]:
a,b,c=4,7,2
if(a<=b and a<=c):
   print(a,"is the smallest")
elif(b<=c and b<=a):
   print(b,"is the smallest")
else:
   print(c,"is the smallest")
2 is the smallest
2.find the GCD and LCM of two/three numbers.

In [6]:
def gcd(a,b):
  if(b==0):
    return a
  else:
    return gcd(b,a%b)
a=int(input())
b=int(input())
GCD=gcd(a,b)
print(GCD)
20
22
2
In [7]:
num1 = int(input())
num2 = int(input())
if(num1 > num2 ):
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break;
    max= max+ 1
10
20
20
3.check whether the given number is perfect.

In [8]:
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(5))
False
4.Print twin primes up to a specified limit

In [25]:
def is_prime(n):
   for i in range(5, n):
      if n % i == 0:
         return False
   return True
 
def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print("{:d} and {:d}".format(i, j))
 
generate_twins(5, 100)
5 and 7
6 and 8
7 and 9
9 and 11
11 and 13
17 and 19
29 and 31
41 and 43
59 and 61
71 and 73
5.Print the prime numbers upto a specified limit

In [12]:
lower = 600
upper = 1000
 
print("Prime numbers between", lower, "and", upper, "are:")
 
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
Prime numbers between 600 and 1000 are:
601
607
613
617
619
631
641
643
647
653
659
661
673
677
683
691
701
709
719
727
733
739
743
751
757
761
769
773
787
797
809
811
821
823
827
829
839
853
857
859
863
877
881
883
887
907
911
919
929
937
941
947
953
967
971
977
983
991
997
6.Find the sum of digits of a number. Check whether given number is Armstrong number or not.

In [13]:
num = int(input("Enter a number: "))
 
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
 
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
Enter a number: 6
6 is not an Armstrong number
In [18]:
num = int(input("Enter a number: "))
 
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
 
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
Enter a number: 54
54 is not an Armstrong number
7.swapping of two number

In [20]:
x = 3
y = 10
 
print ("Before swapping: ") 
print("Value of x : ", x, " and y : ", y) 
 
x, y = y, x 
 
print ("After swapping: ") 
print("Value of x : ", x, " and y : ", y)
Before swapping: 
Value of x :  3  and y :  10
After swapping: 
Value of x :  10  and y :  3
8.Perform all the five arithmetic operations.

In [24]:
a= 50
b = 20
c = 10
 
c = a + b
print ("Addition - Value of c is ", c)
 
c = a - b
print ("Subtraction - Value of c is ", c)
 
c = a * b
print ("Multiplication - Value of c is ", c)
 
c = a / b
print ("Division - Value of c is ", c)
 
c = a % b
print ("Modulus - Value of c is ", c)
Addition - Value of c is  70
Subtraction - Value of c is  30
Multiplication - Value of c is  1000
Division - Value of c is  2.5
Modulus - Value of c is  10