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
"""
from bunch import Bunch


class Memory(Bunch):
    pass


class WorkingMemory(Memory):
    """Working memory is the placeholder for all things.

    When initialized, it makes a copy of any provided ruleset and keeps its
    own copy.
    """
    def __init__(self):
        """Initialize the working memory for a run.

        """
        super(WorkingMemory, self).__init__()
