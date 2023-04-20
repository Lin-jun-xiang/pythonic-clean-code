# python-clean-code

* 本文所定義的並非最佳規範，而是觀察多個大型專案、整理PEP8...風格合併而成
* [Style Guide for Python Code](https://peps.python.org/pep-0008/)

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

# Correct:
s = ' this is a very \
      long string if I had the \
      energy to type more and more ..'
```


### 類、函數

[Ref](https://github.com/googleapis/python-storage/blob/main/google/cloud/storage/client.py)

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
