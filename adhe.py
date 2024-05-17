"""AST2 doesnt have English (UTF-8)"""

import json
import csv


def read_file(file_path: str) -> dict:
    """read json file (return dict)

    Args:
        file_path (str)

    Returns:
        dict: file_d
    """
    with open(file_path, encoding="big5") as f:
        file_j = f.read()
    file_d = json.loads(file_j)
    return file_d


def save_file(file_path: str, obj: dict) -> None:
    """overwrite file with obj input (unicode-escaped)

    Args:
        file_path (str): ouput
        obj (dict): input
    """
    with open(file_path, "w+", encoding="big5") as f:
        f.write(json.dumps(obj, indent=2).encode("ascii").decode("unicode-escape"))


def csv_link(file_d: dict, path: str, init: bool = False) -> None:
    """edit csv link in file_d
        must inculde :
        1.pos.csv
        2.tags.csv
        3.trans.csv
        4.words.csv

    Args:
        file_d (dict)
        path (str)
    """
    file_d["csv"] = path


def add_word(
    word_file_d: dict,
    voc_tar: str,
    pos_tar: str,
    trans_tar: str,
    tags_tar: dict,
    tran_file_d: dict = None,
) -> None:
    """add new word or meaning to word_file_d (or also tran_file_d)

    Args:
        word_file_d (dict)
        voc_tar (str)
        pos_tar (str)
        trans_tar (str)
        tags_tar (dict)
        tran_file_d (dict, optional) Defaults to None.

    Returns:
        _type_: None
    """
    ###add words
    word = word_file_d["words"]
    for vocs in word:
        if voc_tar == vocs["voc"]:  #####################>same word
            for means in vocs["means"]:
                if trans_tar == means["trans"]:  #####################>same word, trans
                    try:  ############################################################=try tags list
                        means["tags"].index(tags_tar)
                    except (  ########################################################>tag diff
                        ValueError
                    ):
                        means["tags"].append(tags_tar)
                    else:  ###########################################################>same word, trans, tag
                        ...
                    break  # jump to next break (10 lines below)
            else:
                vocs["means"].append(  ###############################>mean, tag diff
                    {
                        "pos": pos_tar,
                        "trans": trans_tar,
                        "tags": [tags_tar],
                        "score": "",
                    }
                )
            break  # jump to return
    else:
        word.append(  ###################################>all diff
            {
                "voc": voc_tar,
                "means": [
                    {
                        "pos": pos_tar,
                        "trans": trans_tar,
                        "tags": [tags_tar],
                        "score": "",
                    }
                ],
            }
        )

    if tran_file_d is not None:
        add_word(tran_file_d, trans_tar, pos_tar, voc_tar, tags_tar)

    return None


def add_word_seq(word_file_d: dict, csv_path: str, tran_file_d: dict = None) -> None:
    """add words sequentially using csv (excel available)

    Args:
        word_file_d (dict)
        csv_path (str)
        trans_file_d (dict)
    """
    with open(csv_path, newline="", encoding="big5") as csvfile:
        csv_obj = csv.reader(csvfile, delimiter="|")
        # tags_list = []
        # for row in csv_obj:
        #    tags_list.append(row[3])

        # n = 0
        for row in csv_obj:
            # print(row[0])
            add_word(
                word_file_d,
                clear_space(row[0]),
                clear_space(row[1]),
                clear_space(row[2]),
                json.loads(row[3].replace('""', '"')),
                tran_file_d,
            )
            # n += 1


def clear_space(s: str) -> str:
    """clear tab or space generate from csv reader

    Args:
        string (str)

    Returns:
        str:
    """
    n = 0
    for char in s:
        if char == " ":
            s = s[:n]
        n += 1
    return s


def csv_linker(file_d: dict) -> None:
    """

    Args:
        file_d (dict): _description_
    """
    link = file_d["csv"]
    with open(link + "/words.csv", "w+", newline="", encoding="big5") as csvfile:
        csv_obj = csv.writer(csvfile, delimiter="|")
        csv_obj.writerows(([i["voc"]] for i in file_d["words"]))
    # = [i["voc"] for i in file_d["words"]]
    
    
    
    with open(link + "/pos.csv", "w+", newline="", encoding="big5") as csvfile:
        csv_obj = csv.writer(csvfile, delimiter="|")
        csv_obj.writerows(([i["voc"]] for i in file_d["words"]))

def test(file_d):
    """for test

    Args:
        file_d
    """
    return [(i["voc"]) for i in file_d["words"]]
