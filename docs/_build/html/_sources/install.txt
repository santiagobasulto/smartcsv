.. _install:

Installation
============

This part of the documentation covers the installation of smartcsv.
The first step to using any software package is getting it properly installed.


Distribute & Pip
----------------

Installing smartcsv is simple with `pip <https://pip.pypa.io>`_, just run
this in your terminal::

    $ pip install smartcsv

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install smartcsv

But, you really `shouldn't do that <https://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_.


Get the Code
------------

Smartcsv is actively developed on GitHub, where the code is
`always available <https://github.com/santiagobasulto/smartcsv>`_.

You can either clone the public repository::

    $ git clone git://github.com/santiagobasulto/smartcsv.git

Download the `tarball <https://github.com/santiagobasulto/smartcsv/tarball/master>`_::

    $ curl -OL https://github.com/santiagobasulto/smartcsv/tarball/master

Or, download the `zipball <https://github.com/santiagobasulto/smartcsv/zipball/master>`_::

    $ curl -OL https://github.com/santiagobasulto/smartcsv/zipball/master


Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install
