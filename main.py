import Overheads, CashOnHand,Profit_Loss
from pathlib import Path
from CashOnHand import cash_deficit,cash_surplus_all
from Profit_Loss import pl_deficit,pl_surplus_all
from Overheads import highest_overhead

file_path=Path.home()/'python4biz'/'summary_report.txt'
file_path.touch()
# print(file_path.exists())

with file_path.open(mode='w',encoding='utf-8') as file:
    for deficit in cash_deficit:
        file.writelines(deficit +'\n')
    for surplus in cash_surplus_all:
        file.writelines(surplus+'\n')
    for deficit in pl_deficit:
        file.writelines(deficit +'\n')
    for surplus in pl_surplus_all:
        file.writelines(surplus+'\n')
    for highest in highest_overhead:
        file.writelines(highest+'\n')
    