# python-clean-code
[中文版](README.zh-TW.md) | [English](README.md)

* 本文中的定義不是最佳實踐,而是結合觀察多個大型項目,整理出PEP8,GOOGLE...風格(所以有些可能不符合PEP8)
* 推薦使用`Pylint`、`Pylance`...等相關包查找`bug`和格式問題

* 大綱:
    * [yapf 一鍵格式化](#yapf)
    * [代碼佈局](#code-layout)
        * [字符串](#string)
        * [類,函數](#classfunction)
    * [註釋](#comment)
        * [單行註釋](#one-line)
        * [多行註釋](#multiple-line)
        * [文檔字符串](#docstrings)
    * [類型註解](#type-annotation)
    * [導入順序](#import-oder)
    * [參考](#reference)


## [yapf](https://github.com/google/yapf)

* 使用`yapf` 快速格式化你的代碼. 協同開發更新代碼後推薦使用`yapf`

* 如何使用:
    * `pip install yapf`
    * `yapf -i path/file.py --style='google'`
      
      **style** 包含:
      * `pep8`(default)
      * `google`
      * `yapf`
      * `facebook`

* 之前與之後

   * 前

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

   * 後

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

* Python代碼佈局風格通常是指Python程序員在編寫Python程序時所遵循的代碼風格規範,通常是指PEP 8規範.

* 以下是 Python 程序員普遍遵循的幾個 PEP 8 規範:

* 縮進使用4個空格.不要使用製表符.

* 每行不超過 **79** 個字符. 長行應包含在括號內並在下一行縮進 4 個空格.

* 用空格分隔二元運算符,e.g. **a + b**.

* 將逗號放在最後一個元素之後而不是下一行的開頭. 這允許版本控制系統更好地比較差異.

* 類、函數、方法的定義上方空兩行,類的方法定義之間空一行,函數或方法的局部變量定義前空一行.

* 在一個類中,類名應該使用**`UpperCamelCase`**風格,函數名和方法名應該使用**`lower_case_with_underscores`**風格,變量名也應該使用`lower_case_with_underscores`風格.

* 對文檔字符串使用三引號(""")而不是單引號(''),並且文檔字符串應該縮進一次(與代碼縮進相同).

</details>

### String
* 使用''或"",建議統一使用''

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
s = ' this is a very \//
      long string if I had the \//
      energy to type more and more ..'
```


### Class、function

* 類、函數等代碼塊都需要“**空2行**”。同一個類底下的函數代碼快只需要"**空1行**"
* 注意換行的時機,如下:

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

* 用於解釋文檔程序,通常用於註釋函數
* 如果使用`vscode`編輯器,可以自動生成DocStrings(參考[鏈接](https://github.com/Lin-jun-xiang/vscode-extensions-best#autodocstring---python-docstring-generator))

* `DocStrings example`

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

* `reST`

    ```python
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    ```

* `Google`

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

* `Numpydoc`(推薦！)

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

* 善用 `type annotation`
    * 方便理解函數參數和返回數據類型
    * 有時可以將運行時錯誤轉化為編譯錯誤(提高性能)

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
    * 有時參數類型可以**兩者**都是 `NoneType`,例如 `a` 可以是 `str`、`int`、`NoneType`
    * 現在有以下標準的 `annotaion` 方法:
        * 顯式表達式:`|`
        * `Union`:與顯示表達式相同,例如`Union[str, int, None]`表示參數有三種可能的類型
        * `Optional`:比如`Optional[str]`表示參數是字符串或者`NoneType`

            (如果可以使用`Optional`,就不要使用`Union`)

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

* Blocks:導入模塊順序
    1. `Python` 標準庫(不需要額外的 `pip` 模組)
        `import os`

    2. 第 3 方模組和包
        `import tensorflow as tf`

    3. 代碼倉庫裡的分包(自己開發的)
        `from myproject.ai import mind`

* 每個塊內的模塊順序按字母順序排序

* 如果你使用的是`VSCode`,你可以在編輯器中使用:鼠標右鍵>排序導入

* 導入塊和代碼塊需要“**2個空行**”
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

## Reference
* [PEP8:Python 代碼風格指南](https://peps.python.org/pep-0008/)
* [GOOGLE:風格指南](https://github.com/google/styleguide)

<a href="#top">Back to top</a>
