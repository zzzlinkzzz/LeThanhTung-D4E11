# for i in range(5):
#     print(i)
# print(*range(1,10,3))   # * means print all values

# for i in range(26):
#     print(i)
# for i in range(0,100,2):
#     print(i)
# for i in range(100,0,-1):
#     print(i)

# for i in ['a', 'b', 'c']:
#     print(i)

# n = int(input())
# SUM = 0
# for i in range(n+1):
#     SUM = SUM + i
# print(SUM)

# from turtle import *
# edges = int(input("number of edges >2 : "))
# step = 0
# goto(0,-300)
# for edge in range(3,edges+1):
#     step = step + 10
#     backward(step/2)
#     for i in range(edge):
#         forward(step)
#         left(360/edge)
#     forward(step/2)
# mainloop()

# count = 0
# running = True
# while running:
#     if count == 5:
#         running = False    #or use break
#     print('you can`t stop me')
#     count = count + 1

# username = input("username : ")
# password = input("password : ")

# CheckID = (username == 'mindx' and password == 'password')
# count = 0
# ReSignIn = CheckID == False
# while ReSignIn:
#     if count == 5:
#         print("you are blocked!")
#         break
#     count = count + 1
#     username = input("username : ")
#     password = input("password : ")



username = 'mindx'
password = 'password'
count = 0
while True:
    if count > 7:
        print("you are blocked!")
        break
    ID_input = input("ID : ")
    pass_input = input("Password : ")
    if ID_input == username and pass_input == password:
        print("Welcome")
    count += 1