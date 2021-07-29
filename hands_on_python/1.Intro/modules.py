"""
Importing a module, python search the function at 3 places.
1. Present Working Directory
2. Third party site packages
** Use setUp tool for distribution. 
STEPS: I.
i. create setup.py
ii. create your_function.py
    >>> from setup tools import setup

    >>> setup(
        name = 'your_function',
        ...,
        py_modules = ['your_function'],
    )
iii. create a read me text

II. Generate distribution file
    C:\Users\9701\mymodules> py -3 setup.py sdist #sdist an argument

III. Installation
    c:\dist\> py -3 -m pip install my_function.zip #windows
    $ sudo python3 -m pip install my_function.tar.gz

"""