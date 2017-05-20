# -*- coding: utf-8 -*-
"""Working Memory

From the OPS5 design: Working memory is a global, dynamic user workspace
that contains information about a problem and the current state of its
solution. Information is stored in working memory as objects that are
organized by class. Each working memory object (WMO) has a class name and a
list of associated attributes and their values. The class name classifies
the object according to the type of information it contains. The attributes
and their values describe the object's characteristics. (In database terms,
object classes are like tables and attributes are like fields).

This is structured slightly differently as it leverages the attrs package
to provide a more transparent way to store data through attribute access.
"""
from copy import copy


class WorkingMemory(object):
    """Working memory is the placeholder for all things.

    When initialized, it makes a copy of any provided ruleset and keeps its
    own copy.

    Attributes:
        __rules (list): List of rules we are going to be working
            with. This is done through a copy when initialized so we don't
            end up having to deal with rules being modified on the fly.


    """
    def __init__(self, rules):
        """Initialize the working memory for a run.

        Args:
            rules (List[Rule]): all of the Rule objects to deal with
        """
        # Make a copy so we don't have to deal with potentially mutable
        # rule sets.
        self.__rules = copy(rules)
