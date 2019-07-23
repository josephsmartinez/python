# Object Oriented Python Programming Notes

Single Underscores (weak "internal use" indicator)

Names, in a class, with a leading underscore are simply to indicate to other programmers that the attribute or method is intended to be private. However, nothing special is done with the name itself.

``` py
_function():
```

Double Underscores ()

A double leading underscore actually changes the name of the attribute so that two classes in an inheritance hierarchy can use the same attribute name, and they will not collide.

``` py
__function():
```

Dunder Methods

Special methods are a set of predefined methods you can use to enrich your classes. They are easy to recognize because they start and end with double underscores, for exampl: 

``` py
__init__ or __str__.
```

__funtion__


Resources:

PEP 8 -- Style Guide for Python Code
https://www.python.org/dev/peps/pep-0008/

