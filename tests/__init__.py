import os

from dataclasses import dataclass


@dataclass
class Property:
    browser: str = "chrome"
    test_path = "tests"
    rerun_count = 1
    anyParameter = "aaa"


PROPERTIES = Property()
