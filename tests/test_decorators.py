from pathlib import Path

import pytest

from src.decorators import log


def test_log_prints_success_message_to_console(capsys):
    @log()
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "add_numbers ok\n"


def test_log_prints_error_message_to_console(capsys):
    @log()
    def divide_numbers(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)

    captured = capsys.readouterr()

    assert captured.out == "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_writes_success_message_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(1, 2)

    assert result == 3
    assert log_file.read_text(encoding="utf-8") == "add_numbers ok\n"


def test_log_writes_error_message_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def divide_numbers(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)

    assert (
        log_file.read_text(encoding="utf-8")
        == "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}\n"
    )


def test_log_writes_kwargs_to_error_message(capsys) -> None:
    @log()
    def get_item(items: list[str], index: int = 0) -> str:
        return items[index]

    with pytest.raises(IndexError):
        get_item(["first"], index=2)

    captured = capsys.readouterr()

    assert (
        captured.out
        == "get_item error: IndexError. Inputs: (['first'],), {'index': 2}\n"
    )
