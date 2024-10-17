# unit-testing

I believe in automated testing: unit testing, integration tests, end-to-end tests, and algorithm performance tests. Python gives us the `unittest` and `pytest` libraries which be helpful for automated testing. Here I'll create some pretty trivial examples but in practice I try to always create a minimum of 1 unit test for function.

[unittest examples](https://github.com/merrillmckee/unit-testing/blob/main/src/__tests__/test_my_functions_unittest.py)  
[pytest examples](https://github.com/merrillmckee/unit-testing/blob/main/src/__tests__/test_my_functions_pytest.py)  

of trivial functions

"""
import time


def return_one(num: float) -> float:
    return 1.0


def return_one_slowly(num: float) -> float:
    time.sleep(3.0)
    return 1.0
"""
