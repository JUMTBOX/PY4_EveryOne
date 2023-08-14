# q = ["tr_in", "b_s", "_axi", "air_lane"]
# a = ["a", "u", "t", "p"]

# for i in range(len(q)):
#     question = "%s 에서 밑줄 안에 들어갈 알파벳은?" % q[i]
#     answer = input(question)
#     if answer == a[i]:
#         print("정답입니다.")
#     else:
#         print("오답입니다.")

scoreArr = []

while True:
    score = int(input("성적을 입력하세요(-1입력시 종료) :"))
    if score == -1:
        break
    else:
        scoreArr.append(score)
sum = 0
for score in scoreArr:
    sum = sum + score
avg = sum / len(scoreArr)
print("합계 : %d, 평균: %.2f" % (sum, avg))
