from dataclasses import dataclass
from typing import Any


@dataclass
class TestValue:
    input_value: Any
    expected_output: Any
