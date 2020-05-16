# age = 24
# if age > 18:
#     print('Welcome')
# else:
#     print("You are not allow here")

# score = int(input("add score : "))
# if score >= 9:
#     print("excelent!")
# elif score >=7:
#     print("good!")
# else:
#     print("Bad")

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if delta > 0 :
    result1 = (-b - delta**(1/2))/(2*a)
    result2 = (-b + delta**(1/2))/(2*a)
    print("result1 = ",result1,"result2 = ",result2)
elif delta == 0:
    result = -b/(2*a)
    print("result = ",result)
else:
    print("no result")