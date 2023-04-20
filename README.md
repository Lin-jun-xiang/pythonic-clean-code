# python-clean-code

* The guidelines defined in this article are not the ultimate best practices, but rather a combination of observations from multiple projects and the organization of PEP8 style recommendations.

* [Style Guide for Python Code](https://peps.python.org/pep-0008/)

* [中文版說明書](./README_中文.md)

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

# Correct:
s = ' this is a very \
      long string if I had the \
      energy to type more and more ..'
```

### Class & Function

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
