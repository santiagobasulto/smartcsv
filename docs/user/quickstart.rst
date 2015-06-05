.. _quickstart:

Quickstart
==========

Eager to get started? This page gives a good introduction in how to get started
with smartcsv.

Make sure that smartcsv is :ref:`installed <install>`. In the entire page we'll be supposing we import a CSV with Basketball players.

Defining columns
----------------

Column definition is pretty straightforward, this is a quick example:

::

    # We need to define some stuff first:
    def is_number(n):
        try:
            float(n)
            return True
        except ValueError:
            return False

    COLUMNS = [
        {'name': 'Player Name', 'required': True},
        {'name': 'Home Town', 'required': False},
        {
            'name': 'Player Role/Position',
            'required': True,
            'choices': ['PG', 'SG', 'SF', 'PF', 'C']
        },
        {
            'name': 'age',
            'required': True,
            'validator': is_number,
            'transform': lambda x: Decimal(x)
        },
        {
            'name': 'Profile Image URL',
            'required': False,
            'validator': lambda c: c.startswith('http')
        },
    ]


We've defined our "Column Definition". Now let's feed up a `smartcsv.reader`
