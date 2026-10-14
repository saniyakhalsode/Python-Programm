import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "Check_Even_Odd_Num.py"

spec = importlib.util.spec_from_file_location("even_odd_module", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_even_odd = module.check_even_odd


def test_even_number():
    assert check_even_odd(4) == "Even"


def test_odd_number():
    assert check_even_odd(7) == "Odd"


def test_zero():
    assert check_even_odd(0) == "Even"


def test_negative_even_number():
    assert check_even_odd(-6) == "Even"


def test_negative_odd_number():
    assert check_even_odd(-3) == "Odd"