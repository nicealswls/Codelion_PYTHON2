# 딕셔너리

total_dictionary = {}

while True:
    question = input("질문 입력해 주세용: ")
    if question == 'q':
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해 주세요오: ")
    total_dictionary[i] = answer

print(total_dictionary)        