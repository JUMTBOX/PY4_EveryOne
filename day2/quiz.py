q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}

# for i in q1.keys():
#     if i == "가을":
#         print(q1[i])


# for j, i in q1.items():
#     if i == "사과":
#         print(i, j)
#         break


# def get_maxNum(*args):
#     maxNum = max(args)
#     print(maxNum)


# get_maxNum(55, 66, 77)

# s = "891007-2473837"


# def isMale(str):
#     if int(str[7]) % 2 != 0:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")


# isMale(s)

list = ["A", "b", "c", "D", "e", "F", "G", "h"]

for spell in list:
    if spell.islower():
        print(spell)
    else:
        print(spell.lower())
