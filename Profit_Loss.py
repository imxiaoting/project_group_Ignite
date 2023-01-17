from pathlib import Path
import csv

filepath2=Path.cwd()/'project_group_Ignite/'csv_report_Ignite'/'Profit&Loss1.csv'
filepath2.touch()
#print(filepath2.exists())

with filepath2.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    next(reader)
    

    cluster1=[]
    cluster2=[]

    for day,sales,profit,op,profitloss in reader:
        cluster1.append(day)
        cluster2.append(profitloss)

    # print(cluster2)
    # print(cluster1)

converted3 = [float(num) for num in cluster1]
converted4 = [float(num) for num in cluster2]



one1=1
one=0
days=0
pl_deficit=[]
pl_surplus=[]
pl_surplus_all=[]

while days < len(converted4):
    days+=1
    
    if days<len(converted4):
        if converted4[one]>converted4[one1]:
            pl_deficit.append(f'[Profit Deficit] Day: {converted3[days]}, AMOUNT: ${converted4[one]-converted4[one1]}')
        
            one+=1
            one1+=1
    
        else:
            pl_surplus.append(f'{converted3[days]}')
            one+=1
            one1+=1
            if len(pl_surplus)==len(converted3)-1:
                pl_surplus_all.append(f'[Net Profit SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                

