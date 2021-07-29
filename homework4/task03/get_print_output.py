import sys

"""
Use 2 variables for stdout and stderr
after that check input text to make decision 
where text would be save
"""


def my_precious_logger(text: str) -> None:
    if text.startswith("error"):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
