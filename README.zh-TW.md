# python-clean-code
[中文版](README.zh-TW.md) | [English](README.md)

* 大綱:
    * [簡介](#introduction)
    * [yapf 一鍵格式化](#yapf)
    * [代碼佈局](#code-layout)
        * [類,函數](#classfunction)
    * [評論](#comment)
        * [單行註釋](#one-line)
        * [多行註釋](#multiple-line)
        * [文檔字符串](#docstrings)
    * [類型註解](#type-annotation)
    * [導入順序](#import-oder)
    * [字符串](#string)
    * [命名](#naming)
    * [設計模式](./design-pattern/)
    * [參考](#reference)

## Introduction
* 這篇文章的目的是提高Python Code的能力,讓你寫的代碼更炫,可重用,可維護,可讀性強
* 本文描述的不是最佳實踐,而是多個大型項目的觀察結合.
* 本文將描述
    * python代碼風格
    * python 設計模式
* 推薦使用`Pylint`、`Pylance`...等相關包查找`bug`和格式問題


## [yapf](https://github.com/google/yapf)

* 使用`yapf` 快速格式化你的代碼. 建議協同開發後使用`yapf`更新代碼

* 如何使用:
    * `pip install yapf`
    * `yapf -i path/file.py --style='google'`
    
     **style** 包含:
     * `pep8`(默認)
     * `google`
     * `yapf`
     * `facebook`

* 之前和之後

* 向前

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

* 後退

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

* Python代碼佈局風格通常是指Python程序員在編寫Python程序時遵循的代碼風格規範,通常是指PEP 8規範.

* 以下是Python程序員普遍遵循的幾種PEP 8規範:

* 使用 4 個空格縮進 . 不要使用製表符 .

* 每行不超過 **79** 個字符 . 長行應括在括號中並在下一行縮進 4 個空格 .

* 用空格分隔二元運算符,e.g. **a + b**.

* 將逗號放在最後一個元素之後而不是下一行的開頭 . 這允許版本控制系統更好地比較差異 .

* 類、函數、方法的定義上面有2個空行,類方法定義之間有1個空行,函數或方法的局部變量定義前有1個空行.

* 在一個類中,類名應該使用**`UpperCamelCase`**風格,函數名和方法名應該使用**`lower_case_with_underscores`**風格,變量名也應該使用`lower_case_with_underscores`風格.

* 對文檔字符串使用三引號 (""") 而不是單引號 (''),並且文檔字符串應該縮進一次(與代碼縮進相同).

</details>


### Class、function

* 類、函數等代碼塊需要“**空2行**”. 同一個類下的函數代碼只需要“**空1行**”
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
* 如果使用`vscode`編輯器,可以自動生成DocStrings(參考[鏈接](https://github.com/Lin-jun-xiang/vscode-extensions-best#autodocstring---python-文檔字符串生成器 ))

* %_內聯代碼_%

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

* %_內聯代碼_%

    ```python
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    ```

* %_內聯代碼_%

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
    * 便於理解函數參數和返回數據類型
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

* `Optional` 和 `Union`
    * 有時參數類型可以是**both** `NoneType`,例如`a`可以是`str`、`int`、`NoneType`
    * 現在有以下標準的 `annotaion` 方法:
        * 顯式表達式:`|`
        * `Union`:與顯示表達式相同,例如`Union[str, int, None]`表示參數可能有三種類型
        * `Optional`:比如`Optional[str]`表示參數是字符串或者`NoneType`

            (如果你可以使用 `Optional`,不要使用 `Union`)

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
    1. `Python` 標準庫(不需要額外的 `pip` 模塊)
        `import os`

    2. 第 3 方模組和包
        `import tensorflow as tf`

代碼倉庫裡的    3.分包(自己開發的)
        `from myproject.ai import mind`

* 每個塊中的模塊順序按字母順序排序

* 如果你使用的是`VSCode`,你可以在編輯器中使用:鼠標右鍵>排序導入

* 導入塊和代碼塊需要“**2 空行**”
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
s = ' this is a very \////
      long string if I had the \////
      energy to type more and more ..'
```

* 字符串應使用 `f-string`、`%` 運算符或 `format` 方法. 進行格式化
     即使所有參數都是字符串也為真. 可以判斷合適的選項 . 可以使用+進行單拼接,但是“**不要使用+進行格式化**”.

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

* 不要在循環中使用 + 和 += 運算符堆疊字符串 . 這有時會產生二次而不是線性 **時間複雜度**.
     作為替代方案,您可以將每個子字符串添加到列表中,然後在循環結束後將列表與 `''.join` 連接.
     也可以將每個子字符串寫入一個 `io.StringIO` 緩衝區. 這些技巧保證總是線性攤銷時間複雜度.

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

|類型 |公開 |內部 |
| ---- | --- | ---- |
|包裹| `lower_with_under` | |
|模塊 | `lower_with_under` | `_lower_with_under` |
|類 | `CapWords` | `_CapWords` |
|異常 | `CapWords` | |
|功能 | `lower_with_under()` | `_lower_with_under()` |
|全局常量/類常量 | `CAPS_WITH_UNDER` | `_CAPS_WITH_UNDER` |
|全局變量/類變量 | `lower_with_under` | `_lower_with_under` |
|實例變量 | `lower_with_under` | `_lower_with_under` |
|方法名稱 | `lower_with_under()` | `_lower_with_under()` |
|函數參數/方法參數 | `lower_with_under` | |
|局部變量 | `lower_with_under` | |

<a href="#top">Back to top</a>


## Reference
* [PEP8:Python 代碼風格指南](https://peps.python.org/pep-0008/)
* [GOOGLE:styleguide](https://github.com/google/styleguide)

<a href="#top">Back to top</a>
