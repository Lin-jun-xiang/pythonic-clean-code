# python-clean-code

* 本文所定義的並非最佳規範，而是觀察多個大型專案、整理PEP8、GOOGLE...風格合併而成 (因此有些會與 PEP8 不相符)
* [PEP8: Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [GOOGLE: Style Guides](https://github.com/google/styleguide)
* 建議您使用 `Pylint`, `Pylance` 等相關套件，來尋找 `bug` 與 格式化問題

---

* Outline
    * [yapf 一鍵格式化](#yapf)
    * [代碼布局](#code-layout)
        * [字串](#string)
        * [類、函數](#classfunction)
    * [註釋](#comment)
        * [單行註釋](#one-line)
        * [多行註釋](#multiple-line)
        * [DocStrings](#docstrings)
    * [類型註解](#type-annotation)
    * [導入順序](#import-oder)

---

## yapf

* 使用 `yapf` 可以快速格式化您的代碼，協同開發時建議更新完代碼使用 `yapf`

* 使用方式:
    * `pip install yapf`
    * `yapf -i path/file.py`

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
<a href="#top">Back to top</a>

---

## Code Layout

<details>
<summary>詳細定義</summary>

* Python code layout 風格通常指的是 Python 程序員在編寫 Python 程序時所遵循的程式碼風格規範，通常是指 PEP 8 規範。

* 下面是 Python 程序員通常遵循的幾種 PEP 8 規範：

  * 使用 4 個空格作為縮進。不要使用 tab 字符。

  * 每行不超過 **79** 字符。對於長行，應當在括號內進行折行，並在下一行縮進 4 個空格。

  * 使用空格將二元運算符隔開，例如 **a + b**。

  * 將逗號放在最後一個元素的後面，而不是在下一行開始。這樣可以讓版本控制系統更好地比較差異。

  * 在類、函數和方法的定義上方留出兩行空行，在類的方法定義之間留出一行空行，在函數或方法的局部變量定義之前留出一行空行。

  * 在類中，類名應該使用 **UpperCamelCase** 樣式，函數名和方法名應該使用 **lower_case_with_underscores** 樣式，變量名也應該使用 lower_case_with_underscores 樣式。

  * 對於文檔字符串使用三引號（"""）而不是單引號（''），文檔字符串應縮進一次（與程式碼縮進相同）。

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


### Class、function

* 注意換行時機，如下:

```python
# Wrong:
def long_function_name(
    var_one, var_two, var_three,
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

---

## Comment

### One line

```python
name = 'JunXiang' # 單行註釋

# 單行註釋
name = 'JunXiang'
```

### Multiple line

```python
"""
你好
這是多行註釋
"""
```

### DocStrings

* 用於解釋文檔程序，通常拿來註釋函式
* 如果您使用 `vscode` 編輯器，可以自動生成 DocStrings (參考[連結](https://github.com/Lin-jun-xiang/vscode-extensions-best/blob/main/README_%E4%B8%AD%E6%96%87.md#autodocstring---python-docstring-generator))

* Python Docstrings

    ```python
    def add(num1,num2):
        """ 兩數之和

        :param num1: 數字 1
        :param num2: 數字 2
        :return: 和
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

<a href="#top">Back to top</a>

---

## Type Annotation

* 善用 `type annotation`
    * 方便理解函式參數與回傳的資料型態
    * 有時能將運行時錯誤轉變成編譯錯誤 (提升效能)

```python
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

* `NoneType`
    * 有時候參數類型可以**同時**為 `NoneType`，例如 `a` 可以為 `str`, `int`, `NoneType`
    * 現在的標準 `annotaion` 方式有以下:
        * 顯式表達: `|`
        * `Union`: 與顯示表達一樣，例如 `Union[str, int, None]` 表示參數有三種可能的類型
        * `Optional`: 例如 `Optional[str]` 表示參數要馬字串或`NoneType`

            (可以用`Optional`就不要用`Union`)

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

---

## Import oder

* 區塊: 導入模組順序
    1. `Python` 標準庫 (不需要額外`pip`的模組)
        `import os`

    2. 第三方模組和包
        `import tensorflow as tf`

    3. 代碼倉庫中的子包 (自己開發的)
        `from myproject.ai import mind`

* 各區塊內部模組順序，依照字母排序

* 如果您是使用 `VSCode`，您可以在編輯器中使用: 滑鼠右鍵 > 排序導入

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

```

<a href="#top">Back to top</a>

---