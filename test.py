"""test"""

from adhe import read_file, csv_link, add_word, save_file


wordd = read_file()
# print(wordd)
# print(json.dumps(wordd, indent=4).encode('ascii').decode('unicode-escape')) #wordj

csv_link(wordd, "")

add_word(
    wordd,
    "oval",
    "adj",
    "橢圓形的",
    [{"month": "Feb", "source": "雜", "day": "26", "week": "w4"}],
)


save_file(wordd)
