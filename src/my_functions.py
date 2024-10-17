import time


def return_one(num: float) -> float:
    return 1.0


def return_one_slowly(num: float) -> float:
    time.sleep(3.0)
    return 1.0
