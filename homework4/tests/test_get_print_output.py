from homework4.task03.get_print_output import my_precious_logger


def test_captured_stdout(capsys):
    """Capture what stdout contains"""
    my_precious_logger("text")
    captured = capsys.readouterr()
    assert captured.out == "text"


def test_captured_stderr(capsys):
    """Capture what stderr contains"""
    my_precious_logger("error:very strange task")
    captured = capsys.readouterr()
    assert captured.err == "error:very strange task"
