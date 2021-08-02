from pathlib import Path


def default_tokenizer(text: str):
    """Tokenizer that counts lines in file"""
    text = [line for line in text.split("\n")]
    return text


def universal_file_counter(path_dir: str, extension: str, tokenizer=default_tokenizer):
    """File counter, that will count lines in all files with that extension
    if there are no tokenizer. If a the tokenizer is not none, it will count tokens."""
    directory_path = Path.cwd() / f"{path_dir}"
    if directory_path.exists():
        text = (
            tokenizer(path.read_text())
            for path in directory_path.glob(f"*.{extension}")
        )
        return sum(map(len, text))
    raise IOError("Can't find directory")
