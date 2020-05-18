"""
A Boolean value is either true or false.
1/ 'x' != 'y'
2/ x = 1 y = 1
x != y
3/ char = "gbowuifgwefhwe"
len(char) < 20
"""
"""
flowchart is a kind of chart shows the flow of execution of the program.

input name ===> condition1 == false ====> condition1 == false ====> do nothing
                   ||                         ||
                  true                      true
                   ||                         ||
                   ||                         ||
                    V                          V
            print("Hand some")         even_more_handsome = True 

"""
"""
nested conditionals contain other conditionals inside.
"""
# count = 0
# while True:
#     if count > 3:
#         break
#     count += 1
#     light_input = input("light color? (input red/green) ")
#     if light_input == "red":
#         print("                                                                 stop until the light turns green : ")
#         car_status = input("run for fun or stop like a boss? (input: stop/run)")
#         if car_status == "stop":
#             print("                                                                 good boy!!! you deserve a candy")
#         else:
#             print("                                                                 you are really monkey")
#     else:
#         print("                                                                 beeem! beeem! let's go babe")
#         car_status = input("run for fun or stop like a boss? (input: stop/run)")
#         if car_status == "run":
#             print("                                                                 you look smarter than i thought!!")
#         else:
#             print("                                                                 just another blockhead")

"""draw shapes"""
from turtle import *
speed(-1)

#four rhombus:
# color("red")
# for j in range(4):
#     for i in range(4):
#         if i == 0:
#             left(30)
#         elif i == 2:
#             right(120)
#         else:
#             right(60)
#         forward(100)
#     right(60)
# mainloop()

#polygons
step = 140
goto(0,-300)
for edge in range(15,2,-1):
    if (edge % 2) == 1:
        color("red")
    else:
        color("yellow")
    step += -10
    backward(step/2)
    begin_fill()
    for i in range(edge):
        forward(step)
        left(360/edge)
    end_fill()
    forward(step/2)
mainloop()