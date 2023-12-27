from dataclasses import dataclass


@dataclass
class Property:
    browser: str = "chrome"
    test_path = "tests"
    rerun_count = 1
    qa_url = "https://qaclickacademy.com/practice.php"


PROPERTIES = Property()
