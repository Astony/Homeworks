import sys

"""
Use 2 variables for stdout and stderr
after that check input text to make decision 
where text would be save
"""


def my_precious_logger(text: str):
    stdout_correct_text = sys.stdout
    stderr_error_text = sys.stderr
    if text[0:5] == "error":
        stderr_error_text.write(text)
    else:
        stdout_correct_text.write(text)