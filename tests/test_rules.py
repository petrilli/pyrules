from pyrules.memory import WorkingMemory
import pytest

from .rules import SimplestRule


@pytest.fixture
def working_memory():
    return WorkingMemory()


def test_str(working_memory):
    """Ensure the __str__ rendering is correct"""
    test_rule = SimplestRule(working_memory)

    assert "Test rule" in str(test_rule)


def test_condition(working_memory):
    test_rule = SimplestRule(working_memory)

    assert not test_rule.condition()

    working_memory.test = True

    assert test_rule.condition()
