import csv
import adhe
import json

with open("val.csv", newline="", encoding="big5") as csvfile:
    aaa = csv.reader(csvfile, delimiter="|")
    # print(aaa)
    val_list = []
    for row in aaa:
        row_list = []
        for ele in row:
            # print(row[0])
            row_list.append(ele)
        val_list.append(row_list)
a = json.loads('''{""date"": {""month"": ""Mar"",""day"": ""27"",""week"": ""w4""},""source"": ""雜""} '''.replace('""', '"'))
print(a)
print(type(a))


with open("val.csv", newline="", encoding="big5") as csvfile:
    csv_obj_t = csv.reader(csvfile, delimiter="|")
    tags_list = []
    for row in csv_obj_t:
        tags_list.append(row[3])
print(tags_list[0].replace('""', '"'))
a = json.loads((tags_list[0].replace('""', '"')))
print(a)
print(type(a))

