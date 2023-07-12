"""
Type hinting flake8 plugin tests.

This file was created on July 22, 2021
"""
import ast
from typing import Set

from flake8_typehinting import Plugin


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_trivial_case() -> None:
    """Ensure no errors are thrown if there shouldn't be any."""
    assert _results('') == set()


def test_type_hinting_in_function_definition() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(x="1") -> None:\n    print(x)')
    assert ret == {'1:0 TH100 function missing type hints for arguments (x)'}


def test_type_hinting_in_function_definition_multiple() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(z, y, x="1") -> None:\n    print(x)')
    assert ret == {
        '1:0 TH100 function missing type hints for arguments (x)',
        '1:0 TH100 function missing type hints for arguments (y)',
        '1:0 TH100 function missing type hints for arguments (z)',
    }


def test_type_hinting_in_function_definition_multiple_mixed() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(z, y: int, x="1") -> None:\n    print(x)')
    assert ret == {
        '1:0 TH100 function missing type hints for arguments (x)',
        '1:0 TH100 function missing type hints for arguments (z)',
    }


def test_type_hinting_in_init_function() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def __init__(self, z, y: int, x="1") -> None:\n    print(x)')
    assert ret == {
        '1:0 TH100 function missing type hints for arguments (x)',
        '1:0 TH100 function missing type hints for arguments (z)',
    }


def test_type_hinting_in_function_definition_mixed() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(y: int, x="1") -> None:\n    print(x)')
    assert ret == {'1:0 TH100 function missing type hints for arguments (x)'}


def test_type_hinting_in_function_definition_correct() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(y: int, x: str = "1") -> None:\n    print(f)')
    assert ret == set()


def test_type_hinting_in_function_return() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(y: int, x: str = "1"):  # NOQA: TH101\n    return 1')
    assert ret == {'1:0 TH101 function missing type hints for return value'}


def test_type_hinting_in_function_return_correct() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(y: int, x: str = "1") -> int:\n    return 1')
    assert ret == set()


def test_type_hinting_in_function_definition_cls() -> None:
    """Test type hinting in function definitions."""
    ret = _results('def my_func(cls, y: int, x="1") -> None:\n    print(x)')
    assert ret == {'1:0 TH100 function missing type hints for arguments (x)'}
