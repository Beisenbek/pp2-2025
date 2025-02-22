import re
import csv

f = open("raw.txt", "r",encoding="utf-8")
text = f.read()


BINPattern = r"\nБИН\s(?P<BIN>[0-9]+)"
BINResult = re.search(BINPattern, text).group("BIN")
print(BINResult)

CheckPattern = r"\nЧек\s(?P<Check>№[0-9]+)"
CheckResult = re.search(CheckPattern, text).group("Check")
print(CheckResult)
ItemPattern = r"(?P<ItemRowNumber>.*)\n(?P<ItemName>.*)\n(?P<ItemsCount>.*)\sx\s(?P<ItemPrice>.*)\n(?P<TotalItemPrice1>.*)\nСтоимость\n(?P<TotalItemPrice2>.*)"

prog = re.compile(ItemPattern)
ItemIterator1 = prog.finditer(text)

with open('data.csv', 'w', newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ItemRowNumber', 'ItemName'])
    for ItemResult in ItemIterator1:
         writer.writerow([ItemResult.group("ItemRowNumber"), ItemResult.group("ItemName")])

print("###########################")

ItemIterator2 = prog.findall(text)
for ItemResult in ItemIterator2:
    print(ItemResult[0],ItemResult[1],)