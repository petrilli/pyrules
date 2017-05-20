# -*- coding: utf-8 -*-
import pytest

from pyrules.memory import WorkingMemory


def test_rules_copy():
    fake_rules = [1, 2, 3]
    working_memory = WorkingMemory(rules=fake_rules)

    # Ensure we've got something identical to start with
    assert working_memory._rules == fake_rules

    # Modify our original reference, and ensure they're now different
    fake_rules.append(4)
    assert working_memory._rules != fake_rules
