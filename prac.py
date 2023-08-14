# 변수 명명 규칙
# x = 3
# y = 7
# font1 = "돋움1"
# my_age = 28
# myAge = 28

# 정수타입 = int
# 실수타입 = float

# 소수점n자리까지 출력하는 방법(자동 반올림 됨)
# a = 2 / 3
# print("%.2f" % a)

# b = "안녕"
# print(type(a))
# print(type(b))

# num = 0
# while num < 5:
#     print(num)
#     num += 1
# print("while문 끝남")

# a = 3
# b = 20
# c = b // a
# print(c)

# height = 170
# weight = 64

# bmi = weight / (height**2)

# print(bmi)

# word = "안 녕 !"
# print(word[1:4])


# date = "20191025"
# year = date[0:4]
# month = date[4:6]
# day = date[6:]
# date2 = year + "-" + month + "-" + day

# print(date2)

# msg = "안녕하세요!"
# msgLength = len(msg)

# print("문자열의 길이:%d" % msgLength)


# greeting = input("인사말을 입력하세요::")
# a = input("첫번째 정수를 입력하세요:")
# b = input("두번째 정수를 입력하세요")
# c = int(a) + int(b)

# print(c)

# hp1 = "010"
# hp2 = "1234"
# hp3 = "5678"

# print(hp1, hp2, hp3, sep="-")


# a = 77
# b = "자전거"
# c = 3.3737737
# d = 90
# print("%d,%s,%.2f,%d%%,%6s,%5d," % (a, b, c, d, b, a))

# str = "my name is python"
# print(str.find("n"))


# 문자열 자르기 .split(c)

# str1 = "apple"
# print(str1.split("l"))

# 리스트(배열) 요소를 문자열로 합치기 .join()

# string2 = ["apple", "mango"]
# print("&".join(string2))

color = [
    "red",
    "green",
    "blue",
]

for col in color:
    print("나는 %s색을 가장 좋아합니다." % col)

list = [37, 888, -273, "kim", "hwang", 66.77]

print(list[2:4])
