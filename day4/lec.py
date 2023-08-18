import pandas as pd

dt = pd.read_excel("../sample_excel1.xlsx")
print(dt)

dt["합계"] = dt["인공지능"] + dt["빅데이터분석"] + dt["로봇공학"] + dt["사물인터넷"] + dt["3D프린팅"]
dt["평균"] = dt["합계"] / 5

print(dt)

dt.to_excel("../result.xlsx", sheet_name="성적")
