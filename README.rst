pyversion
=================================
.. image:: https://travis-ci.org/rrajaravi/pyversion.svg?branch=master
    :target: https://travis-ci.org/rrajaravi/pyversion

Version Parser for Python libraries

Installation
------------

-  ``pip install -r requirements.txt``
-  ``python setup.py install``

Example
-------

.. code:: python

    from pyversion import version, get_path, get_dir
    print version('jinja2')
    print get_path('os')
    print get_dir('os')
