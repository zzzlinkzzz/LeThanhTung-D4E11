monan = ['com','pho','bun','mien','banh canh','mi chu']
# # print(monan)

# """
# ICRUD initialize create read update delete
# """
# # create:
# monan.append('mi goi')
# # update:
# monan[0] = 'pho'
# # read:
# for i in range(len(monan)):
#     print(monan[i])
# print(monan.index('banh canh'))
# print('weuyhfvweliuf' in monan)

# for i in range(len(monan)):
#     print(i+1,monan[i])
# update_value = input('nhập tên món ăn muốn đổi? ')
# if update_value in monan:
#     index = monan.index(update_value)
#     monan[index] = input['nhập tên món ăn mới : ']
#     print[monan]
# else:
#     print("không có món đó đâu!!")

# delete:
# monan.pop(0)
# monan.remove('pho')
# """
# xáo trộn thứ tự
# giảm độ dài list
# """
# print(monan)


# import random
# from getpass import getpass
# your_word = getpass("Word to guess? ")
# l = list(your_word)
# random.shuffle(l)
# result = ''.join(l)
# for i in range(len(l)):
#     print(l[i].upper(),end=' ')
# print(result)
# count = 0
# while True:
#     YourGuess = input("enter your answer: ")
#     count += 1
#     if count > 5:
#         print ("you lose!")
#         break
#     if YourGuess == YourWord:
#         print("bingo!")
#         break

# your_word.split(',') # SPLIT BY DELIMITER, ('') => SPLIT ALL character


district = ['ST','BĐ','BTL','CG','ĐĐ','HBT']
areas = [117.43,9.224,43.35,12.04,9.96,10.09]
population = [150300,247100,333300,266800,420900,318000]

min_pop_index = population.index(min(population))
print(min_pop_index)
max_pop_index = population.index(max(population))
print(max_pop_index)

print("min population: ",district[min_pop_index],min(population))
print("max population: ",district[max_pop_index],max(population))

density = []
for i in range(len(district)):
    Den = population[i]/areas[i]
    density.append(Den)
density.sort()
print(density)
avg_density = sum(density)/len(density)
print("Average population density : ",avg_density)