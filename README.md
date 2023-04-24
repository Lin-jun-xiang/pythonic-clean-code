# python-clean-code

* The guidelines defined in this article are not the ultimate best practices, but rather a combination of observations from multiple projects and the organization of PEP8 style recommendations. (Therefore, there're some different with PEP8.)

* [Style Guide for Python Code](https://peps.python.org/pep-0008/)

* [中文版說明書](./README_中文.md)

---

* Outline
    * [yapf 一鍵格式化](#yapf)
    * [Code-Lay-out](#1-code-lay-out)
        * [String](#string)
        * [Class & Function](#class--function)
    * [Comment](#2-comment)
        * [One line comment](#one-line-comment)
        * [Multiple line comment](#multiple-line-comment)
        * [DocStrings](#docstrings)

---

## yapf

* `pip install yapf`

* `yapf -i main.py`

* Before vs After

   * Before
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

      print('ok')
      def some_foo():
          """
          """
          pass
      ```
   
   * After
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

      print('ok')


      def some_foo():
          """
          """
          pass
      ```

---

## 1. Code-Lay-out

<details>
<summary>Details</summary>

* Python code layout style usually refers to the code style guidelines that Python programmers follow when writing Python programs, typically referred to as the PEP 8 guidelines.

* Here are several PEP 8 guidelines that Python programmers usually follow:

  * Use 4 spaces for indentation, not tabs.
  * Keep each line under 79 characters. For long lines, break them at parentheses and indent the continuation line with an additional 4 spaces.
  * Use spaces around binary operators, such as a + b.
  * Put commas at the end of the last item in a sequence, rather than on the next line. This makes it easier for version control systems to compare differences.
  * Leave two blank lines before class, function, and method definitions. Leave one blank line between methods in a class. Leave one blank line before defining local variables in a function or method.
  * Use UpperCamelCase style for class names, lower_case_with_underscores style for function and method names, and lower_case_with_underscores style for variable names.
  * Use triple quotes (""") for docstrings instead of single quotes (''). Docstrings should be indented the same as the code.

</details>

### String

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
s = ' this is a very \
      long string if I had the \
      energy to type more and more ..'
```

### Class & Function

```python
# Wrong:
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# Correct:
def long_function_name(
    var_one, var_two,
    var_three, var_four
):
    print(var_one)

# Better with "annotation and type hint":
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

## 2. Comment

### One line Comment

```python
name = 'JunXiang' # One line Comment

# One line Comment
name = 'JunXiang'
```

### Multiple line Comment

```python
"""
Hi
Multiple line Comment
"""
```

### DocStrings

* Used to explain documentation programs, usually used to annotate functions
* * If you use the `vscode` editor, you can automatically generate DocStrings (see [link](https://github.com/Lin-jun-xiang/vscode-extensions-best#autodocstring---python-docstring-generator))
* Python Docstrings

    ```python
    def add(num1,num2):
        """ Sum of two value

        :param num1: value 1
        :param num2: value 2
        :return: sum
        """
        return num1 + num2

    print( add.__doc__ )
    ```

* reST Docstrings

    ```python
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    ```

* Google Docstrings

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

* Numpydoc (Suggest !)

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
