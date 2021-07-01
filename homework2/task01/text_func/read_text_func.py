import string

"""Read text from txt"""


def read_text_func(file_path: str) -> str:
    with open(file_path, "r") as f:
        text = []
        for lines in f:
            text.append(lines.encode().decode("unicode-escape").strip())
        text = " ".join(text)
        return text
