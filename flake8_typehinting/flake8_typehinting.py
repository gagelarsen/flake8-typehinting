"""
The type hinting flake8 plugin.

This file was created on July 06, 2021
"""
import ast
import sys
from typing import Any, Generator, List, Tuple, Type

if sys.version_info < (3, 8):
    import importlib_metadata  # pragma: no cover
else:
    import importlib.metadata as importlib_metadata  # pragma: no cover

TH100 = 'TH100 function missing type hints for arguments'
TH101 = 'TH101 function missing type hints for return value'


class Visitor(ast.NodeVisitor):
    """
    The visitor class for the type hinting flake8 plugin.
    """

    def __init__(self) -> None:
        """Initialize the visitor class."""
        self.problems: List[Tuple[int, int, str]] = []
        self.import_time_line_num = None

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # NOQA N802
        """Visit function definitions in the ast."""
        self._check_th_100(node)
        self._check_th_101(node)
        self.generic_visit(node)

    def _check_th_100(self, node: ast.FunctionDef) -> None:
        """Check for TH100."""
        for arg in node.args.args:
            if not arg.arg == 'self' and arg.annotation is None:
                self.problems.append((node.lineno, node.col_offset, f'{TH100} ({arg.arg})'))

    def _check_th_101(self, node: ast.FunctionDef) -> None:
        """Check for TH101."""
        if node.returns is None:
            self.problems.append((node.lineno, node.col_offset, TH101))


class Plugin:
    """The Type Hinting flake8 plugin."""
    name = __name__
    version = importlib_metadata.version('flake8_typehinting')

    def __init__(self, tree: ast.AST) -> None:
        """Initialize the flake8 plugin."""
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """Generator for parsing through code."""
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col, msg in visitor.problems:
            yield line, col, msg, type(self)
