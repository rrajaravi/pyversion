pyversion
=================================

Version Parser for Python libraries

Installation
------------

-  ``python -m pip install pyversion``

Example
-------

.. code:: python

    from pyversion import version, get_path, get_dir
    print version('jinja2')
    print get_path('os')
    print get_dir('os')
