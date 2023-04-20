# python-clean-code

* 本文所定義的並非最佳規範，而是觀察多個大型專案、整理PEP8...風格合併而成 (因此有些會與 PEP8 不相符)
* [Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

* Outline
    * [代碼布局](#一代碼布局)
        * [字串](#字串)
        * [類、函數](#類函數)
    * [註釋](#二註釋)
        * [單行註釋](#單行註釋)
        * [多行註釋](#多行註釋)
        * [DocStrings](#docstrings)

---

## 一、代碼布局

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

### 字串

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


### 類、函數

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
```

## 二、註釋

### 單行註釋

```python
name = 'JunXiang' # 單行註釋

# 單行註釋
name = 'JunXiang'
```

### 多行註釋

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

    