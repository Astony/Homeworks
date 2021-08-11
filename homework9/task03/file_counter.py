from pathlib import Path


def universal_file_counter(path_dir: str, extension: str, tokenizer=None):
    """File counter, that will count lines in all files with that extension
    if there are no tokenizer. If a the tokenizer is not none, it will count tokens."""
    directory_path = Path.cwd() / f"{path_dir}"
    if not tokenizer:
        tokenizer = lambda x: x.split("\n")
    if directory_path.exists():
        text = (
            tokenizer(path.read_text())
            for path in directory_path.glob(f"*.{extension}")
        )
        return sum(map(len, text))
    raise IOError("Can't find directory")
