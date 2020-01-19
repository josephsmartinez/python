# Python Unittesting using Mock

## Links

https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832

## About Mock

The main characteristic of a Mock object is that it will return another Mock instance:

- accessing one of its attributes
- calling the object itself

```py
from unittest import mock

m = mock.Mock()
assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)
assert m.foo is not m.bar is not m()
```

You can assign a value to an attribute in the Mock.

```py
m.foo = 'bar'
assert m.foo == 'bar'

m.configure_mock(bar='baz')
assert m.bar == 'baz'
```

To override calls to the mock you’ll need to configure its return_value and/or side_effect.

```py
m.return_value = 42
assert m() == 42

m.side_effect = ['foo', 'bar', 'baz']
assert m() == 'foo'
assert m() == 'bar'
assert m() == 'baz'
try:
    m()
except StopIteration:
    assert True
else:
    assert False

m.side_effect = RuntimeError('Boom')
try:
    m()
except RuntimeError:
    assert True
else:
    assert False
```

Calling function without calling the real fuction.

Note that assert_called_once failed, this showcases another key aspect of Mock objects, they record all interactions with them and you can then inspect these interactions.

```py
m.assert_called()
try:
    m.assert_called_once()
except AssertionError:
    assert True
else:
    assert False
```

For example you can use call_count to retrieve the number of calls to the Mock, and use call_args or call_args_list to inspect the arguments to the last or all calls respectively.
If this is inconvenient at any point you can use the reset_mock method to clear the recorded interactions, note the configuration will not be reset, just the interactions.

```py
try:
    m(1, foo='bar')
except RuntimeError:
    assert True
else:
    assert False
assert m.call_args == mock.call(1, foo='bar')
assert len(m.call_args_list) > 1

m.reset_mock()
assert m.call_args is None
```

MagicMock, a subclass of Mock that implements default magic or dunder methods. This makes MagicMock ideal to mock class behaviour, which is why it’s the default class when patching.

```py
```