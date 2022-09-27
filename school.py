# Made by Moiz patra

# check wether its a prime or not
######################################################
# print("")
# n = int(input("Enter a no."))

# count = 0

# for i in range(1, n, 1):
#     if n%i==0:
#         count = count + 1
        
        

# if count <= 2:
#     print(n," is a prime no.")
# else:
#         print(n," is not a prime no.")

######################################################

# Take input from user and find its sum
######################################################
# print("")
# n = int(input("Enter num 1 :-"))
# m = int(input("Enter num 2 :-"))

# print("Sum of both the number is",n+m)

######################################################

# check if no is odd or even
######################################################
# print("")
# n = int(input("input no."))
# if n % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

######################################################

# print 1 to 10 using while loop
###################################################### 
# n = 1
# while n <= 10:
#     print(n)
#     n = n + 1

######################################################

# print the table of no. user gave
######################################################
# n = int(input("Enter a no."))
# i = 1
# while i < 11:
#     print(n, " X ", i, " = ", n*i)
#     i = i + 1

######################################################

# print the no. of tables user gave[ eg:- 5; table of 1,2,3,4,5]
######################################################
# num = int(input("input no."))

# x = 1

# while x <= num:
#     for i in range(1, 11, 1):
#         print(x, "X", i, "=", x*i , "   ", end='')
        
#     print("")
#     print("Finished the table of ", x)
#     print("")
#     x = x + 1

######################################################

print("")

n = 1

count = 0

print("All prime numbers between 1 to 100 are")
while n <= 100:
    for i in range(1, n+1, 1):
        if n%i==0:
            count = count + 1
            
            
    
    if count <= 2:
        print(n, end='  ')

    count = 0
    n = n +1