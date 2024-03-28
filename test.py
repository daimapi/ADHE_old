"""test (UTF-8)"""

from adhe import read_file, csv_link, add_word, save_file


wordd = read_file()
# print(wordd)
# print(json.dumps(wordd, indent=4).encode('ascii').decode('unicode-escape')) #wordj

csv_link(wordd, "")

add_word(
    wordd,
    "potentially",
    "adv",
    "可能地",
    {"date": {"month": "Mar", "day": "27", "week": "w4"}, "source": "雜"}
)


save_file(wordd)
