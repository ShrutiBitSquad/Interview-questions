# arr = [6, 1, 2, 7, 1, 9, 1, 0, 4, 0, 2, 5]
# dict1={}
# for i in arr:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# for key,value in dict1.items():
#     if value > 1:
#         print(key,"is repeated ", value ,"times")
from datetime import datetime

date_string = "Feb 25 2020 4:20 PM"
date_format = "%b %d %Y %I:%M  %p"
converted_date = datetime.strptime(date_string, date_format)
print(converted_date)

from collections import Counter

arr = [6, 1, 2, 7, 1, 9, 1, 0, 4, 0, 2, 5]
counter = Counter(arr)

for key, value in counter.items():
    if value > 1:
        print(key, "is repeated", value, "times")