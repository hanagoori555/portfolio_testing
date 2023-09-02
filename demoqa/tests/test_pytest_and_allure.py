import allure
import pytest


@pytest.mark.skip(reason="There will be a reason for skipping")
def test_skip():
    assert True


@pytest.mark.xfail(condition=True, reason="The reason why a test function is marked as xfail")
def test_xfail_1():
    """
    test fails - skipped
    test passes - passed
    in both cases - tag "expected failure" in the report
    """
    assert False


@pytest.mark.xfail(condition=True, reason="The reason why a test function is marked as xfail")
def test_xfail_2():
    assert True


@pytest.mark.skipif(condition="2 + 2 != 5")
def test_skip_by_triggered_condition():
    pass


@pytest.mark.parametrize("param", [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0


@allure.title("Skipped test")
@pytest.mark.skip(reason="Reason why skip")
def test_skip():
    assert True


