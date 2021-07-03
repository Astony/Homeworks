import sys

"""
Use 2 variables for stdout and stderr
after that check input text to make decision 
where text would be save
"""


def my_precious_logger(text: str):
    stdout_correct = sys.stdout
    stderr_error = sys.stderr
    if text[0:5] == "error":
        stderr_error.write(text)
    else:
        stdout_correct.write(text)
