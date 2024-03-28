"""AST2 doesnt have English (UTF-8)"""

import json


def read_file() -> None:
    """read json file (return dict)"""
    with open("words.json", encoding="big5") as f:
        word_file_j = f.read()
    word_file_d = json.loads(word_file_j)
    return word_file_d


def save_file(obj: dict) -> None:
    """overwrite file with obj input (unicode-escaped)"""
    with open("words.json", "w+", encoding="big5") as f:
        f.write(json.dumps(obj, indent=2).encode("ascii").decode("unicode-escape"))


def csv_link(word_file_d: dict, edit_d: str) -> None:
    """edit csv link in word_file_d"""
    word_file_d["csv"] = edit_d


def add_word(
    word_file_d: dict, voc_tar: str, pos_tar: str, trans_tar: str, tags_tar: dict
) -> None:
    """add new word or meaning to word_file_d"""
     
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

    return None
