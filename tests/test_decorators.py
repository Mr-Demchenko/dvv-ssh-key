from pathlib import Path

import pytest

from decorators import log


def test_log_prints_success_message_to_console(capsys):
    @log()
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(1, 2)
    captured = capsys.readouterr()

    captured_lines = captured.out.strip().splitlines()

    assert result == 3
    assert len(captured_lines) == 3
    assert captured_lines[0].startswith("start add_numbers in ")
    assert captured_lines[1].startswith("Result of add_numbers in ")
    assert captured_lines[1].endswith(" is 3")
    assert captured_lines[2].startswith("end add_numbers ")


def test_log_prints_error_message_to_console(capsys):
    @log()
    def divide_numbers(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)

    captured = capsys.readouterr()

    captured_lines = captured.out.strip().splitlines()

    assert len(captured_lines) == 3
    assert captured_lines[0].startswith("start divide_numbers in ")
    assert captured_lines[1] == "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}."
    assert captured_lines[2].startswith("end divide_numbers ")


def test_log_writes_success_message_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(1, 2)

    assert result == 3
    log_lines = [line.rstrip() for line in log_file.read_text(encoding="utf-8").splitlines()]

    assert len(log_lines) == 3
    assert log_lines[0].startswith("start add_numbers in ")
    assert log_lines[1].startswith("Result of add_numbers in ")
    assert log_lines[1].endswith(" is 3")
    assert log_lines[2].startswith("end add_numbers ")


def test_log_writes_error_message_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def divide_numbers(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)

    log_lines = [line.rstrip() for line in log_file.read_text(encoding="utf-8").splitlines()]

    assert len(log_lines) == 3
    assert log_lines[0].startswith("start divide_numbers in ")
    assert log_lines[1] == "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}."
    assert log_lines[2].startswith("end divide_numbers ")


def test_log_writes_kwargs_to_error_message(capsys) -> None:
    @log()
    def get_item(items: list[str], index: int = 0) -> str:
        return items[index]

    with pytest.raises(IndexError):
        get_item(["first"], index=2)

    captured = capsys.readouterr()

    captured_lines = captured.out.strip().splitlines()

    assert len(captured_lines) == 3
    assert captured_lines[0].startswith("start get_item in ")
    assert captured_lines[1] == "get_item error: IndexError. Inputs: (['first'],), {'index': 2}."
    assert captured_lines[2].startswith("end get_item ")
