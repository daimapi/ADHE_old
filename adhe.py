"""AST2 doesnt have English"""

# UTF-8
import json


def read_file() -> None:
    """read json file (return dict)"""
    with open("words.json", encoding="big5") as f:
        wordj = f.read()
    wordd = json.loads(wordj)
    return wordd


def save_file(obj: dict) -> None:
    """overwrite file with obj input (unicode-escaped)"""
    with open("words.json", "w+", encoding="big5") as f:
        f.write(json.dumps(obj, indent=2).encode("ascii").decode("unicode-escape"))


def csv_link(wordd: dict, _dict: str) -> None:
    """edit csv link in wordd"""
    wordd["csv"] = _dict


def add_word(wordd: dict, tarvoc: str, pos: str, trans: str, tags: list) -> None:
    """add new word or meaning to wordd"""
    word = wordd["words"]
    for voc in word:
        if voc["voc"] == tarvoc:
            voc["means"].append({"pos": pos, "trans": trans, "tags": tags, "score": ""})
            return None
    word.append(
        {
            "voc": tarvoc,
            "means": [{"pos": pos, "trans": trans, "tags": tags, "score": ""}],
        }
    )
    return None
