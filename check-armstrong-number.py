#python program to check armstrong number

#input from user
n = int(input("Enter the number : "))

#initialize the sum
sum = 0

#check sum for the cube of each digit
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
#print the result
if n == sum:
    print(" is an Armstrong number", n)
else:
    print(" is not an Armstrong number", n)