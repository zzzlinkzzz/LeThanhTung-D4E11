# # =============================================
"""         turtle draw        """

# from turtle import *
# speed(-1)
# color("blue")

# for retangle in range(28):
#     for edge in range(4):
#         forward(100)
#         left(90)
#     left(360/28)
# mainloop()

# edge_length = 0
# for retangle in range(35):
#     edge_length += 10
#     for edge in range(4):
#         forward(edge_length)
#         left(90)
#     left(360/35)
# mainloop()

# # =============================================
"""     standardise user’s name     """

# name = str(input("enter a name? ")).lower().split(' ')
# name = [char for char in name if char != '']
# for i in range(len(name)):
#     name[i] = name[i].capitalize()
# print(' '.join(name))

# # =============================================
"""      standardise balance account    """

# balance = int(input("enter your balance? "))
# print('$','{:0,.0f}'.format(balance))

# # =============================================
"""       Serious exercises 1           """
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# # add key 'pocket'
# inventory['pocket'] = ['seashell','strange berry','lint']
# # remove dagger
# inventory['backpack'].remove('dagger')
# # add more gold
# inventory['gold'] +=50
# for key in inventory:
#     print(key,inventory[key])

# # =============================================
"""       Serious exercises 2           """

# import random
# numbers = [random.randrange(0,10,1) for x in range(300)]
# print(numbers)
# distinct = list(set([str(i) for i in numbers]))
# distinct.sort()
# print("numbers in list: ",' '.join(distinct))
# try:
#     num = int(input("enter a number ?"))
#     count = len([x for x in numbers if x == num])
#     print(str(num)," appears ",str(count)," times in my list")  
# except:
#     print("i know it is not a number, dude!!!")

# # =============================================
"""       Serious exercises 3           """

# init_num = int(input("how many B bacterias are there? "))
# times = int(input("how much time in minutes will we wait? "))
# print("after",str(times),"minutes, we would have",str((times//2)*2*init_num),"bacterias")

# # =============================================
"""       Serious exercises 4           """

# mature = 1
# baby = 0
# months = int(input("how many months? "))
# for month in range(months):
#     if month != 0:
#         pre_mature = mature
#         mature += baby
#         baby = pre_mature
#     print("Month",str(month),": ",str(baby + mature)," pairs of rabbit")

# # =============================================
"""       Serious exercises 5           """

# prices = {
#     'banana': 4,
#     'apple': 2,
#     'orange': 1.5,
#     'pear': 3
# }
# stock = {
#     'banana': 6,
#     'apple': 0,
#     'orange': 32,
#     'pear': 15
# }
# for key in prices:
#     print("*   ",key,"\n*    price:",prices[key],"\n*    stock:",stock[key],'\n ')

# total = 0
# for key in prices:
#     total += prices[key]*stock[key]
# print("*    revenue_forcast: ",total)