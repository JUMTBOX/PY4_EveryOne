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


# def oddEven(n):
#     if n % 2 == 0:
#         print("%d --> 짝수입니다." % n)
#     else:
#         print("%d --> 홀수입니다." % n)


# oddEven(3)


# 인자를 여러개 받을 때
# def argFunc(*args):
#     print(args)
#     for t in args:
#         print(list(t))


# argFunc("yang")


# 중첩 함수


# def deps1(num1):
#     def deps2(num2):
#         print(num2)

#     print("in function")
#     deps2(num1 + 100)


# deps1(50)


# def sum(start, end):
#     hap = 0
#     for i in range(start, end + 1):
#         hap += i
#     print("%d ~ %d의 정수의 합계: %d" % (start, end, hap))


# sum(1, 100)
