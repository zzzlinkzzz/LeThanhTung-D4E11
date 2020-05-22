# from turtle import *
# speed(-1)
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# step = 50
# for edge in range(3,8):
#     step = step + 10
#     backward(step/2)
#     color(colors[edge-3])
#     for i in range(edge):
#         forward(step)
#         left(360/edge)
#     forward(step/2)
# mainloop()

# length = int(input("length = "))
# goto(-length*5/2,-length/2)
# for i in range(5):
#     color(colors[i])
#     begin_fill()
#     for edge in range(4):
#         if edge % 2 == 0:
#             forward(length)
#         else:
#             forward(length*2)
#         left(90)
#     end_fill()
#     forward(length)
# mainloop()

# import random
# sheeps = [random.randrange(50,400,1) for x in range(10)]
# months = int(input("how many months? "))
# for month in range(months):
#     print("MONTH ", month+1,":")
#     for i in range(len(sheeps)):
#         sheeps[i] += 50
#     print(" One month has passed, now here is my flock: ", sheeps)
#     if month+1 != months:
#         print("My biggest sheep has size ",max(sheeps)," let's shear it")
#         sheeps[sheeps.index(max(sheeps))] = 8
#         print("After shearing, hear is my flock: ", sheeps)
#     else:
#         print("My flock has size in total: ", sum(sheeps))
#         print("I would get ",sum(sheeps)," * $2 = $",sum(sheeps)*2)

import random
text = "These kindergarten vocabulary words introduce and reinforce high-utility words. The majority of words in each Flocabulary kindergarten video are considered tier-2-vocabulary—high-utility and aspirational words that are relevant to academic success. Many of these songs are thematically tied to units that are taught at the early elementary grade levels (the four seasons, primary geography terms, animals and their characteristics) to streamline learning. Flocabulary's kindergarten videos each revolve around a specific setting or concept (a visit to the dentist, surfing on the beach). While several of the words are specific to that setting (healthy, rotten, row) others are more general purpose words (gentle, relax, glance) that have meaning within the specific story, but have wider application as well."
text_list = text.split(" ")
count1 = 0
while True:
    count1 += 1
    if count1 > 3:
        break

    picked = text_list[random.randrange(0,len(text_list),1)].lower()
    l = list(picked)
    random.shuffle(l)
    result = ' '.join(l)
    print(result)
    count2 = 0
    while True:
        YourGuess = input("enter your answer: ").lower()
        count2 += 1
        if count2 > 2:
            print ("you lose!")
            break
        if YourGuess == picked:
            print("bingo!")
            break

