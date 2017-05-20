=======
pyrules
=======


.. image:: https://img.shields.io/pypi/v/pyrules.svg
        :target: https://pypi.python.org/pypi/pyrules

.. image:: https://img.shields.io/travis/petrilli/pyrules.svg
        :target: https://travis-ci.org/petrilli/pyrules

.. image:: https://pyup.io/repos/github/petrilli/pyrules/shield.svg
     :target: https://pyup.io/repos/github/petrilli/pyrules/
     :alt: Updates


A Python rules engine inspired by OPS5, because sometimes you just want to have a basic rule system that you can run against data, and you don't want to have to deal with the crazy of CLIPS.
This will never be designed for dealing with thousands of rules against hundreds of thousands of facts.
What it does, hopefully, is allow you to abstract out the design of rules, and not worry so much about the flow.

The system uses a basic model of rule engine execution, rather than the more advanced Rete_ model.
It uses a simple conflict resolution model, and opportunistic matching by the rules, with a combination of refraction, arbitrary choice, and declarative ordering.


* Free software: BSD license


Features
--------

* Uses a simple recognize-act cycle.


Recognize-Act Cycle
-------------------

The recognize-act cycle is the pattern-matching procedure that takes place repeatedly as a ruleset program executes.
The design is based on the idea that once working memory is populated, the rules are run until none match any more, or an iteration limit is reached.
The cycle consists of the following steps:

1. Match: Iterate through each rule, allowing it to search working memory and decide if it has something to offer.
   This places all instantiations in a list called the conflict set.
2. Select: Using an ordered sequence of criteria, specifically combining refraction, declarative ordering, and optional arbitrary choice, take the instantiation with the highest priority out of the conflict set.
   If the conflict set is empty (because no rule condition has been satisfied), the cycle stops.
3. Act: Execute the actions of the rule in the selected working memory.


Installation
------------

TODO


Usage
-----

TODO


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Rete: https://en.wikipedia.org/wiki/Rete_algorithm

