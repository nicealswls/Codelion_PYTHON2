from stat import IO_REPARSE_TAG_APPEXECLINK


# 딕셔너리를 빈 리스트에 추가해 주는 형태

total_list = [] # 빈 리스트 생성

while True:
    question = input("질문을 입력해 주세요: ")
    if question == 'q':
        break
    else: 
        total_list.append({"질문": question, "답변": ""}) # key와 value 형태, 리스트에 딕셔너리 만들어 항목 추가함

for i in total_list:
    print(i["질문"]) 
    answer = input("답변을 입력해 주세요 제발: ")
    i["답변"] = answer
print(total_list)           