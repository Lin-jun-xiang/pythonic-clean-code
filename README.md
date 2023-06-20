# python-clean-code
[中文版](README.zh-TW.md) | [English](README.md)

* Outline:
    * [Introduction](#introduction)
    * [yapf one-key formatting](#yapf)
    * [code layout](#code-layout)
        * [class, function](#classfunction)
    * [comment](#comment)
        * [single-line comment](#one-line)
        * [multiple-line comment](#multiple-line)
        * [docstrings](#docstrings)
    * [type annotation](#type-annotation)
    * [import order](#import-oder)
    * [string](#string)
    * [naming](#naming)
    * [design pattern](./design-pattern/)
    * [reference](#reference)

## Introduction
* The purpose of this article is to improve the ability of Python Code, so that the code you write is more dazzling, reusable, maintainable and readable
* What this article describes is not a best practice, but a combination of observations from multiple large projects .
* This article will describe
    * python code style
    * python design patterns
* It is recommended to use `Pylint`, `Pylance`... and other related packages to find `bug` and format problems


## [yapf](https://github.com/google/yapf)

* Use `yapf` to quickly format your code . It is recommended to use `yapf` to update the code after collaborative development

* how to use:
    * `pip install yapf`
    * `yapf -i path/file.py --style='google'`
    
     **style** contains:
     * `pep8` (default)
     * `google`
     * `yapf`
     * `facebook`

* before and after

* forward

        ```python
        import pandas as pd


        class MyClass(object):
            def __init__(self, some_value: int):
                self.value = some_value
            def one_more_function(self, another_value):
                print(another_value)
        myObject = MyClass(45)
        myObject.one_more_function(2)
        my__object2 = MyClass(324)


        def some_foo():
            """
            """
            pass
        ```

* back

        ```python
        import pandas as pd


        class MyClass(object):

            def __init__(self, some_value: int):
                self.value = some_value

            def one_more_function(self, another_value):
                print(another_value)


        myObject = MyClass(45)
        myObject.one_more_function(2)
        my__object2 = MyClass(324)


        def some_foo():
            """
            """
            pass
        ```

<a href="#top">Back to top</a>


## Code Layout

<details>
<summary>More</summary>

* Python code layout style usually refers to the code style specification that Python programmers follow when writing Python programs, usually refers to the PEP 8 specification.

* The following are several PEP 8 specifications that Python programmers generally follow:

* use 4 spaces to indent . do not use tabs .

* No more than **79** characters per line . Long lines should be enclosed in parentheses and indented 4 spaces on the next line .

* Separate binary operators with spaces, e.g. **a + b**.

* Put the comma after the last element instead of the beginning of the next line . This allows version control systems to better compare diffs .

* There are 2 blank lines above the definitions of classes, functions, and methods, 1 blank line between class method definitions, and 1 blank line before the definition of local variables of functions or methods .

* In a class, class name should use **`UpperCamelCase`** style, function name and method name should use **`lower_case_with_underscores`** style, variable name should also use `lower_case_with_underscores` style .

* Use triple quotes (""") instead of single quotes ('') for docstrings, and docstrings should be indented once (same as code indentation) .

</details>


### Class、function

* Classes, functions and other code blocks need "**empty 2 lines**" . function codes under the same class only need "**empty 1 line**"
* Pay attention to the timing of line breaks, as follows:

```python
# Wrong:
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)


# Correct: (yapf)
def long_function_name(var_one,
                       var_two,
                       var_three:,
                       var_four):
    print(var_one)


# Correct: (google)
def long_function_name(
    var_one, var_two,
    var_three, var_four
):
    print(var_one)
```

<a href="#top">Back to top</a>


## Comment

### One line

```python
name = 'JunXiang' # Comment

# Comment
name = 'JunXiang'
```

### Multiple line

```python
"""
Hi
Comment
"""
```

### DocStrings

* Used to explain documentation programs, usually used to annotate functions
* If you use the `vscode` editor, DocStrings can be automatically generated (refer to [link](https://github.com/Lin-jun-xiang/vscode-extensions-best#autodocstring---python-docstring Builder))

* %_inline code_%

    ```python
    def add(num1,num2):
        """ sum of two value

        :param num1: value 1
        :param num2: value 2
        :return: 和
        """
        return num1 + num2


    print( add.__doc__ )
    ```

* %_inline code_%

    ```python
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    ```

* %_inline code_%

    ```python
    """
    This is a groups style docs.

    Parameters:
    param1 - this is the first param
    param2 - this is a second param

    Returns:
    This is a description of what is returned

    Raises:
    KeyError - raises an exception
    """
    ```

* `Numpydoc` (recommended!)

    ```python
    """My numpydoc description of a kind
    of very exhautive numpydoc format docstring.

    Parameters
    ----------
    param1 : int
        this is the first param
    param2 : int, Optional
        this is a second param

    Returns
    -------
    This is a description of what is returned

    Raises
    ------
    KeyError
    when a key error
    OtherError
    when an other error
    """
    ```

<a href="#top">Back to top</a>


## Type Annotation

* Make good use of `type annotation`
    * facilitates understanding of function parameters and return data types
    * can sometimes turn runtime errors into compile errors (improves performance)

    ```python
    from typing import Optional, Union


    # Better with "annotation and type hint": (google)
    def long_function_name(
        var_one: int,
        var_two: str = 'default',
        var_three: Optional[str] = None,
        var_four: Optional[int] = None
    ) -> None:
        """A example"""
        print(var_one)


    # yapf
    def long_function_name(var_one: int,
                        var_two: str = 'default',
                        var_three: Optional[str] = None,
                        var_four: Optional[int] = None) -> None:
        """A example"""
        print(var_one)
    ```

* `Optional` and `Union`
    * Sometimes the parameter type can be **both** `NoneType`, for example `a` can be `str`, `int`, `NoneType`
    * now have the following standard `annotaion` methods:
        * explicit expression: `|`
        * `Union`: Same as the display expression, for example, `Union[str, int, None]` indicates that there may be three types of parameters
        * `Optional`: For example, `Optional[str]` indicates that the parameter is a string or `NoneType`

             (if you can use `Optional`, don't use `Union`)

    ```python
    # Wrong: don't use Union if you can use Optional
    def func(a: Union[None, str]) -> srt:
        ...

    # Wrong: implicit is not good choice (It's not recommend after PEP 484 )
    def func(a: str = None) -> str:
        ...

    # Correct: use explicit method
    def func(a: str | int | None, b: str | None = None) -> str:
        ...

    # Correct: use Union and Optional
    def func(a: Union[str, int, None], b: Optional[str] = None) -> str:
        ...

    ```

<a href="#top">Back to top</a>


## Import oder

* Blocks: import module order
    1. `Python` standard library (no extra `pip` module required)
        `import os`

    2. 3rd party mods and packs
        `import tensorflow as tf`

    3. subcontracting in the code warehouse (developed by myself)
        `from myproject.ai import mind`

* The order of modules within each block is sorted alphabetically

* If you are using `VSCode`, you can use in the editor: right mouse button > sort import

* import blocks and code blocks require "**2 blank lines**"
```python
# Block 1
import collections
import os
import sys

# Block 2
from absl import app
from absl import flags
import bs4
import cryptography
import tensorflow as tf

# Block 3
from myproject.backend import huxley
from myproject.backend.hgwells import time_machine
from myproject.backend.state_machine import main_loop
from otherproject.ai import body
from otherproject.ai import mind
from otherproject.ai import soul


...your code
```

<a href="#top">Back to top</a>


## String

* Use '' or "", it is recommended to use '' uniformly

```python
# Wrong:
s ='this is a very long string if I had the energy to type more and more ...'

# Correct:
s = """ this is a very
        long string if I had the
        energy to type more and more ..."""

# Correct:
s = ("this is a very"
     "long string too"
     "for sure ..."
    )

# Correct (PEP8 not suggest):
s = ' this is a very \/////
      long string if I had the \/////
      energy to type more and more ..'
```

* String should be formatted using `f-string`, `%` operator or `format` method .
     is true even if all parameters are strings . can determine the appropriate option . can use + for single splicing, but "**do not use + for formatting**" .

```python
# Correct
x = f'名称: {name}; 分数: {n}'
x = '%s, %s!' % (imperative, expletive)
x = '{}, {}'.format(first, second)
x = '名称: %s; 分数: %d' % (name, n)
x = '名称: %(name)s; 分数: %(score)d' % {'name':name, 'score':n}
x = '名称: {}; 分数: {}'.format(name, n)
x = a + b

# Wrong
x = first + ', ' + second
x = '名称: ' + name + '; 分数: ' + str(n)
```

* Do not stack strings using + and += operators in loops . this sometimes produces quadratic instead of linear **time complexity** .
     As an alternative, you can add each substring to a list, then concatenate the list with `''.join` . after the loop is over
     can also write each substring to a `io.StringIO` buffer . These tricks guarantee always linear amortized time complexity .

```python
# Correct
items = ['<table>']
for last_name, first_name in employee_list:
    items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
items.append('</table>')
employee_table = ''.join(items)

# Wrong
employee_table = '<table>'
for last_name, first_name in employee_list:
    employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
employee_table += '</table>'
```

<a href="#top">Back to top</a>

## Naming

|Type |Public |Internal |
| ---- | --- | ---- |
|package|`lower_with_under`||
|Module | `lower_with_under` | `_lower_with_under` |
|class | `CapWords` | `_CapWords` |
|Exception | `CapWords` | |
|Function | `lower_with_under()` | `_lower_with_under()` |
|Global constant/class constant | `CAPS_WITH_UNDER` | `_CAPS_WITH_UNDER` |
|Global variables/class variables | `lower_with_under` | `_lower_with_under` |
|Instance variables | `lower_with_under` | `_lower_with_under` |
|Method name | `lower_with_under()` | `_lower_with_under()` |
|Function parameter/method parameter | `lower_with_under` | |
|local variables | `lower_with_under` | |

<a href="#top">Back to top</a>


## Reference
* [PEP8:Python Code Style Guide](https://peps.python.org/pep-0008/)
* [GOOGLE:styleguide](https://github.com/google/styleguide)

<a href="#top">Back to top</a>
