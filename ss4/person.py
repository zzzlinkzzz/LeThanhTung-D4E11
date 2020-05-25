# person = ['Đạt',96,'Viettel',1, True, False]
# person = {
#     'name': 'Đạt', 
#     'yob': {
#         'year': 1996,
#         'month': 1,
#         'day': 1
#     }, 
#     'company': ['Viettel','Vinaphone'],
#     'key': None
# }
# # print(person['name'])
# # print(person['yob']['year'])

# person['relationship'] = True
# person['yob']['month'] = 4
# del person['key']
# for key in person:
#     print(key,":",person[key])

TeenCode = {
    'hc': 'học',
    'pt': 'phát triển',
    'ns': 'năm sinh',
    'stt': 'số thứ tự'
}
# while True:
#     print('  '.join(list(teen_code.keys())))
#     search = input("your code? ")
#     if  search in teen_code:
#         print('trans: ',teen_code[search])
#         print("*"*30)
#     else:
#         ask = input("not found, do you want to contribute this words? (Y/N)").lower()
#         if ask in ['y','yes']:
#             meaning = input("enter your trans: ")
#             teen_code[search] = meaning
#             print("updated")
#         print("*"*30)


# sentence = input("enter a sentence: ").lower()
# list_char = list(set(sentence))
# list_char.sort()
# for char in list_char:
#     print(char,sentence.count(char))

char_summary = {}
sentence = input("enter a sentence: ").lower()
sorted_sentence = sorted(sentence)
for char in sorted_sentence:
    if char in char_summary:
        char_summary[char] += 1
    else:
        char_summary[char] = 1
for key in char_summary:
    print(key,char_summary[key])