Nonsense Project in order to learn git and Python packaging in detail
--------

To use (with caution), simply do::

    >>> import funniest
    >>> print funniest.joke()

# Folowing along tutorial on:
# https://python-packaging.readthedocs.io/en/latest/minimal.html






-StructuringProject/ (funniest) # toplevel directory e.g. funniest.git
    -dist # created via python setup.py sdist
    -funniest/ # actual Python module
        -tests/ # should be in subdict of module, such that they can be imported but won't pollute global namespace
            -__init__.py
            -test_joke.py
        -__init__.py
        -text.py # in general additional files should go here and are called from __init__.py
    -setup.py
    -bin/
        - funniest-joke
    -.gitignore # contains: compiled python .pyc, distribution folder, egg metadata

https://python-packaging.readthedocs.io/en/latest/everything.html
funniest/
    funniest/
        __init__.py
        command_line.py
        tests/
            __init__.py
            test_joke.py
            test_command_line.py
    MANIFEST.in
    README.rst
    setup.py
    .gitignore