.. smartcsv documentation master file, created by
   sphinx-quickstart on Fri Sep  5 11:53:07 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

smartcsv: Smart CSV files for humans
====================================

Release v\ |version|. (:ref:`Installation <install>`)

`smartcsv` is a small utility that will make your life easier when handling CSV files. This is a quick example:

::

    >>> reader = smartcsv.reader(file_object, columns=COLUMNS, fail_fast=False)
    >>> my_object = next(reader)
    >>> my_object['title']  # Accessed by model name.
    'iPhone 5c Blue'
    >>> my_object['price']  # Value transform included
    Decimal("799.99")
    >>> my_object['currency']  # Based on choices = ['USD', 'YEN']
    'USD'
    >>> my_object['url']  # custom validator lambda v: v.startswith('http')
    https://www.apple.com/iphone.jpg

    # Nice errors
    >>> from pprint import pprint as pp
    >>> pp(my_object.errors)
    {
        17: {  # The row number
            'row': ['','',...]  # The complete row for reference,
            'errors': {  # Description of the errors
                'url': 'Validation failed',
                'currency': 'Invalid choice. Expected ['USD', 'YEN']. Got 'AUD' instead.
            }
        }
    }

For more examples like this, see :ref:`examples <examples>`.

Contents:

.. toctree::
  :maxdepth: 2

  user/install
  user/quickstart
  user/examples


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

