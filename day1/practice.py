# q = ["tr_in", "b_s", "_axi", "air_lane"]
# a = ["a", "u", "t", "p"]

# for i in range(len(q)):
#     question = "%s 에서 밑줄 안에 들어갈 알파벳은?" % q[i]
#     answer = input(question)
#     if answer == a[i]:
#         print("정답입니다.")
#     else:
#         print("오답입니다.")

# scoreArr = []

# while True:
#     score = int(input("성적을 입력하세요(-1입력시 종료) :"))
#     if score == -1:
#         break
#     else:
#         scoreArr.append(score)
# sum = 0
# for score in scoreArr:
#     sum = sum + score
# avg = sum / len(scoreArr)
# print("합계 : %d, 평균: %.2f" % (sum, avg))


# scores = [[10, 20, 30], [40, 50, 60, 70]]

# for i in range(len(scores)):
#     sum = 0
#     for j in range(len(scores[i])):
#         sum += scores[i][j]

#     avg = sum / len(scores[i])

#     print("%d번째 학생의 합계: %d, 평균: %.2f" % (i + 1, sum, avg))

# nums = (2, 3, 4, 5, 6, 7, 8, 9)

# print("구구단표")
# print("=" * 50)

# for dan in nums:
#     print(str(dan) + "단")
#     for i in range(1, 10):
#         print("%d x %d = %d" % (dan, i, dan * i))

# print("-" * 30)

# user = {"name": "yang", "age": 28}
# del user["age"]
# print(user)
