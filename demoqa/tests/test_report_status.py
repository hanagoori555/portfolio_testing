import pytest
import allure


@allure.feature("Checking test statuses")
def test_success():
    assert True


@allure.feature("Checking test statuses")
def test_failure():
    assert False


@allure.feature("Checking test statuses")
def test_skip():
    pytest.skip("...")


@allure.feature("Checking test statuses")
def test_broken():
    raise Exception("O-ops...")
