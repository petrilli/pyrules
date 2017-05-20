# -*- coding: utf-8 -*-
"""Rule definitions

Rules are the core of the system. They express specifically what we want
to happen as data is processed.  The RuleEngine runs in a slightly modified
version of the OPS5 model, but Rules generally follow.
"""
from weakref import proxy
from .memory import WorkingMemory


class Rule(object):
    """Foundational rule object.

    A Rule has a name, and it consists of a conditional test, often called
    the left-hand side (LHS), and an action, often called the right-hand
    side (RHS). The conditional test examines the WorkingMemory, and
    decides whether it may need to take an action.  The RuleEngine will
    then execute the action of the Rule that it selects.
    """
    __name__ = "Name of the Rule"

    def __init__(self, working_memory):
        """Instantiate the rule.

        We keep a weak-ref proxy to the WorkingMemory so that we don't create
        any non-GCable garbage.

        Args:
            working_memory (WorkingMemory): In-flight work for this Rule
        """
        self.__wm = proxy(working_memory)
        super(Rule, self).__init__()


    def condition(self):
        """Predicate to decide if this rule needs to be applied.

        To do this, it should examine the in-flight instance of
        WorkingMemory.

        Returns:
            bool: True if action should be taken, False otherwise
        """
        raise NotImplemented

    def action(self):
        """Take action on the working memory.

        Returns:
            bool: True if action succeeded and rule should be kept in, False
                if the rule should be removed from consideration.
        """
        raise NotImplemented
