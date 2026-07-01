from typing import Dict

def add_bonus(grades : Dict[str,float], bonus: float) -> None:
        for student in grades:
            grades[student] += bonus