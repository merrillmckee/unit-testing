import pytest
import time

from my_functions import return_one, return_one_slowly
from unittest.mock import Mock, patch  # unittest is only used for mocking


def test_return_one():
    # arrange
    input_num = 1.234  # for this trivial example, the test input doesn't matter
    expected_result = 1.0

    # act
    result = return_one(input_num)

    # assert
    assert result == pytest.approx(expected_result)


@patch("my_functions.time.sleep")
def test_return_one_slowly(sleep: Mock):
    # same test as above except we don't want to wait on the full call stack of the function we are testing.
    #   that call stack may be calling functions that are already unit tested. Or the call stack may be
    #   reaching out to IO (files, db). for both performance, determinism, and not wanting to repeat test
    #   coverage, we patch this called function.

    # mock
    sleep.return_value = None

    # arrange
    input_num = 1.234  # for this trivial example, the test input doesn't matter
    expected_result = 1.0

    # act
    start = time.time()
    result = return_one_slowly(input_num)
    elapsed_time = time.time() - start

    # assert
    assert result == pytest.approx(expected_result)
    assert elapsed_time < 1.0  # asserting speed just to show the 3-second sleep is being mocked


if __name__ == "__main__":
    pytest.main()  # output below

    # ============================= test session starts =============================
    # collecting ... collected 2 items
    #
    # test_my_functions_pytest.py::test_return_one PASSED                      [ 50%]
    # test_my_functions_pytest.py::test_return_one_slowly PASSED               [100%]
    #
    # ============================== 2 passed in 0.05s ==============================
    #
    # Process finished with exit code 0

