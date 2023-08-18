# from pandas import DataFrame

# sdata = {
#     "사원": ["강덕구", "이유란", "서수길", "강구열", "김윤환"],
#     "실적": [800, 200, 500, 400, 700],
#     "분기": [1, 2, 3, 1, 2],
# }

# myIndex = ["하나", "둘", "셋", "넷", "다섯"]
# myFrame = DataFrame(sdata, index=myIndex)

# print(myFrame)

# -----------------------------------------------------------------
import numpy as np
from pandas import DataFrame

# myData = np.arange(9).reshape(3, 3)

# myFrame = DataFrame(myData, index=["용산구", "마포구", "은평구"], columns=["김철수", "이영희", "정준수"])

# print(myFrame)

# -----------------------------------------------------------------

sdata = {"지역": ["용산구", "마포구"], "연도": [2019, 2020]}
sframe = DataFrame(sdata)

print(sframe)

# -----------------------------------------------------------------
