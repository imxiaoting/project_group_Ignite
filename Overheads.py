from pathlib import Path
import csv

file_path_overheads=Path.home()/'python4biz'/'py files'/'csv files'/'Overheads1.csv'
file_path_overheads.touch()
# print(file_path_overheads.exists())

with file_path_overheads.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    next(reader)

    
    Cluster6=[]

    for num in reader:
        
        Cluster6.append(num)


Cluster6.sort(key=lambda value:value[1],reverse=True)
highest_overhead=[]
highest_overhead.append(f'[HIGHEST OVERHEADS] {Cluster6[0][0]}: {Cluster6[0][1]}')

# def sort(Cluster6):
#     length = len(Cluster6)
#     for num in range(0, length):
#         for num1 in range(0, length-num-1):
#             if (Cluster6[num1][1] > Cluster6[num1 + 1][1]):
#                 sum = Cluster6[num1]
#                 Cluster6[num1]= Cluster6[num1 + 1]
#                 Cluster6[num1 + 1]= sum
#     return Cluster6


                













