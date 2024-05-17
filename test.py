"""test (UTF-8)"""

# from adhe import *  # read_file, csv_link, add_word, save_file, add_word_seq

import adhe as ad

words_d = ad.read_file("./data1/words to trans.json")
trans_d = ad.read_file("./data1/trans to words.json")
# print(wordd)
# print(json.dumps(wordd, indent=4).encode('ascii').decode('unicode-escape')) #wordj

ad.csv_link(words_d, "./data1/keys")
ad.csv_link(trans_d, "./data1/keys")

ad.add_word(
    words_d,
    "potentially",
    "adv",
    "可能地",
    {"date": {"month": "Mar", "day": "27", "week": "w4"}, "source": "雜"},
    trans_d,
)

ad.add_word_seq(words_d, "./val.csv", trans_d)

#ad.csv_linker(words_d)
print(ad.test(words_d))

ad.save_file("./data1/words to trans.json", words_d)
ad.save_file("./data1/trans to words.json", trans_d)
