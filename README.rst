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

* TODO


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

