# -*- coding: utf-8 -*-
from pyrules.rules import Rule


class SimplestRule(Rule):
    __name__ = "Test rule"

    def condition(self):
        if hasattr(self._wm, 'test'):
            return True
        return False

    def action(self):
        return True
