# 조건문
# x = int(input("필기 점수를 입력하세요"))
# y = int(input("실기 점수를 입력하세요"))
# if x < 80 and y < 70:
#     print("불합격 입니다.")
# else:
#     print("합격입니다.")

# 반복문
# for x in range(5):
#     print("for문 입니다.")


# word = input("영어 문장을 입력하세요")

# for x in word:
#     print(x)

# i = 0
# while i < len(word):
#     print("while문 입니다.")
#     i += 1


# 함수
# def hello(name):
#     val = ""
#     print("안녕", name)
#     return val


# str = hello("재연")

# print(str)


# def inputNum():
#     n = input("자연수를 입력하세요: ")
#     while not n.isdigit():
#         print("자연수를 입력하여주세요")
#         n = input()
#     print("입력된 값: ", n)


# inputNum()


def oddEven(n):
    if n % 2 == 0:
        print("%d --> 짝수입니다." % n)
    else:
        print("%d --> 홀수입니다." % n)


oddEven(3)
