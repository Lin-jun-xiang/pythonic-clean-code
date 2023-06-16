# Design Pattern
[中文版](README.zh-TW.md) | [English](README.md)

* A design pattern is a summary of a set of code design experiences that are repeatedly used, known to most people, cataloged, and coded.
* The use of design patterns is to reusable code, to make the code easier for others to understand, and to ensure code reliability.
* interface = interface, object = object
* Precognition: object orientation, category and object, variable and immutable objects, Pass by Assignment, Decorator. [Reference Notion]()


* Outline:
    * base feed
        * [Introduction to Object Oriented and Design Patterns](#introduction)
            * [Object Oriented Outline](#intro-oop)
            * [Introduction to Design Pattern](#intro-design-pattern)
        * [inherited]()
        * [abstract class, interface](#abstractorinterface)
        * [polytype]()
        * [encapsulation](#encapsulation)
    * [23 Design Patterns](https://jasonblog.github.io/note/design_pattern/index.html)
     : emoji_heavy_check_mark: commonly used
        * **creative mode**
            * [Singleton](#singleton)
            * [Abstract Factory](#)
            * [Builder](#)
            * [Factory Method](#)
            * [Prototype](#)
        * **structural mode**
            * [Adapter](#)
            * [Bridge](#)
            * [Composite](#)
            * [Decorator](#decorator):heavy_check_mark:
            * [Facade](#)
            * [Flyweight](#)
            * [Proxy](#)
        * **Behavior Pattern**
            * [Template Method](#)
            * [Command](#)
            * [Interpreter](#)
            * [Mediator](#)
            * [Iterator](#)
            * [Observer](#)
            * [Chain Of Responsibility](#)
            * [Memento](#)
            * [State](#)
            * [Strategy](#strategy):heavy_check_mark:
            * [Visitor](#)
    * special design
        * [MVC (evolved from Observer, Strategy, Composite)](#mvc):heavy_check_mark:
        * [MVP](#mvp):heavy_check_mark:
        * [MVVM](#mvvm):heavy_check_mark:
    * [reference](#reference)


## Introduction

#### Intro-OOP

Basic principles (1~5 also known as SOLID)

* **Single Responsibility Principle (SRP: Single Responsibility Principle)** A category should have only one reason for its change
* **Open, closed principle (OCP: Open Closed Principle)** is open for extension (open for extension) and closed for modification (closed for modification)
* **Liskov Substitution Principle (LSP: Liskov Substitution Principle)** The subcategory must be able to replace the parent category.
* **Interface Segregation Principle (ISP: Interface Segregation Principle)**
* **Dependency Inversion Principle (DIP: Dependency Inversion Principle)** Abstraction should not depend on details, details should depend on abstraction. Because the image is relatively stable. High-level modules should not depend on low-level modules, both should depend on abstractions. Program to interfaces, not to concrete implementations.
* **Law of Demeter (LoD: Law of Demeter)** Principle of Least Knowledge Only talk to your immediate friends Only talk to your immediate friends Low coupling

     For example: The postman sends a registered letter, and the recipient's seal needs to be affixed. Most people will not ask the postman to go into the house to find the seal by himself, which is a waste of time and unsafe. Usually, I go into the house to get it by myself, or ask other family members to help me get it. Because the postman should not be given the authority to enter the house to find things, and the postman does not need to know where the seal is placed in the house.
* **Composition/Aggregation Reuse Principle (CARP)(Composite/Aggregate Reuse Principle)** Use more synthesis/aggregation and less inheritance. When two objects have a has-a (has-parts, is-part-of) relationship => composition/aggregation (A has a B) When two objects have an is-a (is-a-kind-of) relationship Time => Inheritance (Superman is a kind of Person)
    * Composite (Composite): When two objects A and B have a composite relationship, it means that one of the objects disappears (ex: emoji_book), and the other object also disappears (ex: chapter).
    * Aggregate (Aggregate): When the two objects A and B have an aggregation relationship, it means that one of the objects disappears (ex: emoji_team), and the other object does not disappear (ex: player).

<a href="#top">Back to top</a>

#### Intro-Design Pattern

* Creational Pattern
    * **Simple Factory pattern** Use the static method of class to obtain different objects according to different conditions, and use the obtained objects to do similar things. The disadvantage is that when you want to add different conditions, you must modify the static method of the category.
    * **Factory Method Pattern (Factory Method Pattern)** avoids the simple factory pattern. When adding conditions, modify the static method of the factory class (the modification should be closed).
    * **Abstract Factory Pattern (Abstract Factory Pattern)** Abstract factory category, which can return the same type of factory. These return factories, with multiple identical methods, that do similar things.
    * **Builder Pattern (Builder Pattern)** sorts out the production steps of a certain type of product construction process, and all classes that want to produce this type of product must implement these standardized steps. In addition, in order to avoid missing a certain step during actual production, a series of production steps are performed by a single commander class.
    * **Prototype Pattern (Prototype Pattern)** Copy an existing object to generate a new object. Shallow clone: Only the properties of the old object are copied, and the objects in the old object are not copied. So new and old objects will share these other objects. Deep clone: The attributes in the old object and other referenced objects will be copied.
    * **Singleton Pattern** Allows a category to have only one instance (Instance) method. The way to generate a single instance: Lazy initialization: The instance is only generated when it is used for the first time. Eager initialization: An instance is generated when the class is loaded, regardless of whether it will be used later.

* Structural Pattern
    * **Adapter Pattern** An existing class, the interface is not what the user expects. The adapter is used as an intermediate interface to provide the interface expected by the user. It can be divided into two implementation methods Object Adapter Pattern (Object Adapter Pattern): Wrap the existing class instance in the adapter category. Class Adapter Pattern (class adapter pattern): use multiple inheritance.
    * **Bridge Pattern (Bridge Pattern)** extracts the specific behavior (implementation) of an object and becomes an independent object. That is, the original one object becomes two objects: "abstract object" + "real object". The advantage is that abstract objects and real objects can be decoupled and changed independently.
    * **Composite Pattern** Between several objects, there is a tree structure.
    * **Decorator Pattern (Decorator Pattern)** Dynamically add functions to an object. Functions are applied layer by layer, and each layer implements different objects.
    * **Facade Pattern** Package the original large system and open it to users with another simpler interface. Users only need to know how to use the interface. It is not necessary to understand the operation mode of each small system in the large system.
    * **Flyweight Pattern** Between objects, if there are common parts that can be shared, the shareable parts will be separated as shared objects, and the non-shareable parts will be externalized, and then used Externalized parts are passed to shared objects. This has the advantage of reducing memory usage. The disadvantage is that the program logic may become more complex.
    * **Proxy Pattern (Proxy Pattern)** There are two objects, the proxy object and the real object. The system uses the proxy object to operate, and the real object is operated inside the proxy object. Application: remote agent, virtual agent, security agent

* Behavioral pattern
    * **Chain-of-responsibility Pattern** There are several objects that can handle a certain request, but the scope of processing (permissions) is different. When this object does not have processing permissions, it can Pass this request to the next object to continue processing.
    * **Command Pattern (Command Pattern)** General commands include issuing commands and executing commands. The command mode is to split this process into three objects, the object that issues the command (Invoker), the object that executes the command (command), and the object that executes the command (receiver). The Invoker object is used to build the command to be executed. In this way, when it is necessary to expand the function, such as adding repeated execution of commands, canceling commands ..., etc., it becomes simpler.
    * **Interpreter Pattern (Interpreter Pattern)** is used to explain and translate a language.
    * **Iterator Pattern (Iterator Pattern)** A method of traversing the elements in the container.
    * **Mediator Pattern** When there may be intricate interactions between objects, these relationships can be handed over to another object (mediator) to reduce the interaction between these objects coupling.
    * **Memento Pattern (Memento Pattern)** A method to restore an object to its previous state.
    * **Observer Pattern (Publish/Subscribe Mode) (Observer Pattern)** Two types of objects, "notifier" and "observer".
        * Subscription: "Notifier" can add or remove "Observer" in the subscription list
        * Release: When an event to be monitored occurs, the "notifier" can notify the "observer" of the event from the subscription list, and the "observer" will take corresponding actions on the event.
        * Function: decoupling, so that both sides of the coupling rely on abstraction (interface) instead of concrete.
    * **State Pattern (State Pattern)** An object has multiple states, and has different behaviors in different states. Generally, multiple if elses may be used to handle these branching behaviors. If the state mode is used, these states are processed and extracted to another class to process these branches. That is, if else is rewritten as a class.
    * **Strategy Pattern** defines different algorithms as a family. These algorithms implement the same interface and are written as individual categories, so they can replace each other. The advantage is that if you want to add a new algorithm in the future, you only need to add an additional category without moving the original category.
    * **Template Method Pattern** Move the unchanging part to the parent category, and remove the repeated code in the subcategory
    * **Visitor Pattern (Visitor Pattern)** When the "elements" in an "object structure" hardly change, but these "behaviors of elements" often increase or decrease, the visitor pattern is suitable. The visitor mode is to extract the "behavior of elements", and each behavior is made into a "Visitor (visitor) object". Each "Visitor (visitor) object" can be different from the original "object structure". "elements" that produce different behaviors.

<a href="#top">Back to top</a>

## Abstractor、Interface

Compared with java, python strictly distinguishes between abstraction and interface. Python has no native abstract categories and methods, and must use the abc package to implement abstract categories and interfaces. In Python, whether it is an abstract class or an interface, it inherits abc.ABC.
(`C:\/Users\/junxianglin\/AppData\/Local\/Programs\/Python\/Python38\/lib\/abc.py`)

* Abstract category (abstractor)
Abstraction of     * classes
    * **Categories that cannot be materialized**
    * When a method (Method) is covered with a `@abc.abstractmethod` decorator (decorator), it means that the establishment of an abstract method must rely on subcategory override.

        ```python
        from abc import ABC, abstractmethod
        class Animal(ABC): # python 中繼承 abc.ABC,表示該類別為抽象類別,不可直接實體化
            def __init__(self, name="john", shout_num=1):
                self.name = name
                self.shout_num = shout_num
            def run(self):
                """ implement run behavior"""
                print('run')
            @abstractmethod
            def shout(self): # 套上抽象類別修飾器,該方法為抽象方法,不可直接實體化,僅定義方法,實際內容由子類別覆寫
                pass
            
        class Dog(Animal):
            def __init__(self, name, shout_num):
                super().__init__(name, shout_num)
            def shout(self):
                print('wo' * self.shout_num)
        class Cat(Aniamal):
        ...
        dog = Dog('daniel', 3)
        dog.run() # run
        dog.shout() # wowowo
        animal = Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods shout
        ```

* Interface/Interface (Interface)
Abstraction of     * behavior

* Abstract base class (abstractor basic class, abc)
     Suppose we want to develop a data interface with three functions: connect to the database, read data, and execute SQL. These functions can be defined through ABC first, and then the subclass is responsible for implementing (overriding)
    ```python
    from abc import ABC
    from abc import abstractmethod
    ​
    ​
    class Database(ABC):
        def register(self, host, user, password): # register是每個子類都需要的,直接實現在abc裡面
            print("Host : {}".format(host))
            print("User : {}".format(user))
            print("Password : {}".format(password))
            print("Register Success!")
    ​
        @abstractmethod
        def query(self, *args):
            """
            传入查询数据的SQL语句并执行
            """
    ​
        @staticmethod
        @abstractmethod
        def execute(sql_string):
            """
            sql...
            """

    class Component1(Database):
        def __init__(self, host, user, password):
            self.register(host, user, password)

        @staticmethod
        def execute(sql_string):
            print(sql_string)

        def query(self, *args):
            sql_string = "SELECT ID FROM db_name"
            self.execute(sql_string)


    class Component2(Database):
        def __init__(self, host, user, password):
            self.register(host, user, password)
    
        @staticmethod
        def execute(sql_string):
            print(sql_string)
    
        def query(self, *args):
            sql_string = "SELECT NAME FROM db_name"
            self.execute(sql_string)

    comp1 = Component1("00.00.00.00", "abc", "000000")
    comp2 = Component2("11.11.11.11", "ABC", "111111")
    comp1.query()
    comp2.query()
    ```


<a href="#top">Back to top</a>

## Encapsulation

* The purpose of encapsulation is to prevent the outside from having any chance to change the object in an unexpected way. Encapsulation can strengthen the robustness of the object.
* There is a `property` decorator in python that can turn a method into an attribute, which is equivalent to encapsulating this attribute. The outside world does not need to know the implementation method to get this attribute, and it will not be changed arbitrarily.

```python
class Product():
    @property
    def price(self):
        return 100
Product().price # 100
Product().price = 150 # AttributeError: can't set attribute

class Product():
    def __init__(self):
        self._price = 100
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    
product = Product()
product.price = 150
product.price # 150
```

<a href="#top">Back to top</a>

## Singleton

* Singleton

## Decorator

* Decorator mode (Decorator)
* Focus on "**adding new functions**" to the object dynamically under the premise of "**not modifying the original object or function**"
* When to use: **Multiple functions need to do some pre- or post-work**, which can be decorated uniformly, such as logging verification
* Features:
    * does not modify the source code of existing functions
    * does not modify the calling method of existing functions
    * add extra functionality to existing functions
* New functions built in Python can be extended to existing objects through `＠`
* Common extension categories are: **data verification (pydantic)**, **Caching**, Logging, Monitoring, **Debugging**, Business Rules, Excryption, Compression…

<details>
<summary>Timeit</summary>

* does not change the original object f1
* Before executing f1: write down the time
* After executing f1: record the time and print out the execution time of f1
* Matching timing: multiple functions need to record the execution time

    ```python
    from functools import wraps
    import time

    def timeit(func):
        @wraps(func)
        def wrapper(*arg, **kwarg):
            time_start = time.time()
            value = func(*arg, **kwarg)
            time_end = time.time()
            time_spend = time_end - time_start

            print(f"[{func.__name__}] function cost time: {time_spend}")

            return value

        return wrapper

    @timeit
    def f1(t):
        time.sleep(t)
        print("End~")

    f1(1)
    f1(2)
    ```
</details>

<details>
<summary>Property</summary>



</details>

<details>
<summary>Cache</summary>

* Through the cache mechanism, write down the calculation process, and **avoid repeated calculations** when encountering repeated processes (streamlit can also use `@cache` to process load data)
* Store the calculation results that are frequently used repeatedly in the memory with faster access speed to speed up the way to obtain the results.
* When the amount of data is large, you will encounter the problem of memory occupation, which is a double-edged sword

* Customize a simple cache decorator to improve the performance of computing cost arrays. Repeated fib(i) is obtained through cache

    ```python
    from functools import wraps 

    def cache(func): 
        caches = {} 
        @wraps(func) 
        def wrap(*args): 
            if args not in caches: 
                caches[args] = func(*args) 
            return caches[args] 
        return wrap 

    @cache 
    def fib(n): 
        if n < 2: 
            return 1 
        return fib(n-1) + fib(n-2)
    ```

* `functools.lru_cache(maxsize)`
    * implements the cache function based on the least recently used (LRU) algorithm, and automatically manages the cache size (**automatically delete the least used**)
    * maxsize defines the depth of recursion that only needs to be noted

        ```python
        from functools import lru_cache

        @lru_cache(maxsize=100)
        def fib(n): 
            if n < 2: 
                return 1 
            return fib(n-1) + fib(n-2)
        ```

    * **Applicable to any repeated calculation function**

        ```python
        from functools import lru_cache

        @lru_cache(maxsize=3)
        def add(a, b):
            print("Calculating...")
            return a + b

        print(add(1, 2))  # Calculating... 3
        print(add(1, 2))  # 3 (from cache)
        print(add(3, 4))  # Calculating... 7
        print(add(5, 6))  # Calculating... 11
        print(add(3, 4))  # 7 (from cache)
        ```

    * Modified "return variable object" function, need to use copy. [Reference](https://www.zhihu.com/question/350078061)

        ```python
        from functools import lru_cache
        from copy import deepcopy

        def copying_lru_cache(maxsize=10, typed=False):
            def decorator(f):
                cached_func = lru_cache(maxsize=maxsize, typed=typed)(f)
                def wrapper(*args, **kwargs):
                    return deepcopy(cached_func(*args, **kwargs))
                return wrapper
            return decorator


        @copying_lru_cache()
        def cached_function(param):
            print(f"running cached_function on: {param}")
            return np.array([param])


        for number in [100, 100, 100, 200]:
            res = cached_function(number)
            res *= 5
            print(f"number: {number}, result: {res}")
        ```
</details>

<details>
<summary>Debugging</summary>

* Debug is usually assisted by `print`, as you can see from the following function, we will invasively modify the object, and eventually have to remove print, which is quite inconvenient

    ```python
    def sum(a, b):
        print("a=", a)
        print("b=", b)
        print("a+b=", a+b)
        return a+b
    ```

* via debug decorator

    ```python
    def sum(a, b):
        return a + b

    def debug(func):
        print('func name: ', func.__name__)
        def wrapper(*args, **kwargs):
            print('args', args)
            print('kwargs', kwargs)
            result = func(*args, **kwargs)
            print(func.__name__, '=', result)
        return wrapper

    debug_sum = debug(sum)
    debug_sum(1, 2)

    """
    func name: sum
    args (1, 2)
    kwargs {}
    sum = 3
    """
    ```

</details>

<details>
<summary>Decorator with parameters</summary>

* Add one more layer of decorator
* before limiting the output k

    ```python
    from functools import wraps

    def limitOutput(dec_arg=0):
        def callable(func):
            @wraps(func)
            def wrapper(*arg, **kwarg):
                v = func(*arg, **kwarg)

                return v[:dec_arg]
            return wrapper
        return callable

    @limitOutput(10)
    def exec():
        return [i for i in range(100)]

    exec()
    ```

</details>

<details>
<summary>Multi Decorator</summary>

* Execution order of multiple decorators

    ```python
    @decorator_a
    @decorator_b
    def f(x):
        print('running f.')

    # decorator b running.
    # decorator b finished.
    # decorator a running.
    # decorator a finished.
    ```
</details>

## Strategy

* Strategy mode (Strategy)

* Belongs to Behavior Mode, which converts a set of **behaviors into objects**

* Focus on choosing different algorithms or behaviors at runtime, **In the face of different situations, you need to make different behaviors, that is, strategies**
    * There are many sorting algorithms, we can choose different algorithms according to the data size

* Scenario: The big data system pushes the files, and adopts **different analysis** according to different types
    * non-design mode
         Disadvantages: The code is bloated, and when the type is adjusted, it needs to be changed to the original code
        ```python
        if ():
            ...
        elif ():
            ...
        else ():
            ...
        ```
    * strategy pattern
        * `ParserStrategy`: The abstract base class of the strategy, each specific parsing strategy inherits the behavior defined by this class `parse`
        * `ParserContext`: parsed context class, select the corresponding strategy according to the incoming data type
        ```python
        from abc import ABC, abstractmethod

        class ParserStrategy(ABC): # 定義抽象基類,不可實例化
            @abstractmethod
            def parse(self, data):
                pass

        class Type1Parser(ParserStrategy):
            def parse(self, data):
                # 执行 Type1 解析逻辑
                print("Type1 解析")

        class Type2Parser(ParserStrategy):
            def parse(self, data):
                # 执行 Type2 解析逻辑
                print("Type2 解析")

        class ParserContext:
            def __init__(self, strategy):
                self.strategy = strategy

            def set_strategy(self, strategy):
                self.strategy = strategy

            def parse_data(self, data):
                self.strategy.parse(data)

        # 示例用法
        data = get_data_from_big_data_system()  # 从大数据系统获取数据

        # 创建解析策略实例
        type1_parser = Type1Parser()
        type2_parser = Type2Parser()

        # 创建上下文对象并设置默认解析策略
        context = ParserContext(type1_parser)

        # 根据不同类型选择解析策略
        if is_type1_data(data):
            context.set_strategy(type1_parser)
        elif is_type2_data(data):
            context.set_strategy(type2_parser)

        # 解析数据
        context.parse_data(data)
        ```
<details>
<summary>場景: 不同類型的付費</summary>

```python
class ParserStrategy:
    def parse(self, data):
        raise NotImplementedError

class Type1Parser(ParserStrategy):
    def parse(self, data):
        # 执行 Type1 解析逻辑
        print("Type1 解析")

class Type2Parser(ParserStrategy):
    def parse(self, data):
        # 执行 Type2 解析逻辑
        print("Type2 解析")

class ParserContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def parse_data(self, data):
        self.strategy.parse(data)

# 示例用法
data = get_data_from_big_data_system()  # 从大数据系统获取数据

# 创建解析策略实例
type1_parser = Type1Parser()
type2_parser = Type2Parser()

# 创建上下文对象并设置默认解析策略
context = ParserContext(type1_parser)

# 根据不同类型选择解析策略
if is_type1_data(data):
    context.set_strategy(type1_parser)
elif is_type2_data(data):
    context.set_strategy(type2_parser)

# 解析数据
context.parse_data(data)
```

</details>


## MVC

* **File Separation**: Put codes with different functions in different files

     (three folders: Model, View, Controller)

* Three structures
    * Model: responsible for communicating with the database
    * View: Responsible for managing the rendering of the screen, that is, the HTML template (template)
    * Controller: Program logic, the bridge between M and V. The request from the route will be sent to the Controller first, and then the Controller will notify the Model to schedule the data, and pass the data to the View to generate a template (template)

        <img src='img/2023-06-16-11-28-31.png' width='60%' />

* Router vs Controller

    * Router: work assignment, put the corresponding URI and controller into routes[]
    * Controller: Responsible for the work, execute the communication between M and V

     (When developing API, you only need to focus on using Router to separate different api routes)

* advantage
    * Very intuitive, easy to understand
    * Use Controller to separate Model and View, with a certain degree of decoupling
* shortcoming
    * **The three depend on each other**, once one of them is updated, the other two must be modified accordingly
    * With continuous development and adding functions, **Controller code will become more and more bloated**
    * are difficult to unit test

## MVP

* In order to improve the shortcomings of MVC, replace Controller with Presenter
* The difference from MVC is that after the Model layer gets the data, it does not directly pass it to the View for update, but returns it to the Presenter, and the Presenter then passes the data to the View and updates the screen. (From the interdependence of the three to the interdependence of the two)

    <img src='img/2023-06-16-11-34-12.png' width='60%' />

* advantage
    * from the interdependence of the three to only rely on the Presenter (there are fewer places to change)
    * Clear responsibility and clear division of labor
    * View is only responsible for calling Presenter to get data after receiving user feedback, and updating the screen when receiving data.
    * Model passively receives the Presenter command, gets the data, and sends it back to the Presenter.
    * Presenter communicates with View and Model through the interface, and is the only link window between View and Model.
    * is convenient for unit testing
        
        Because the Presenter operates the View through the interface, when performing a unit test on the Presenter that does not depend on the UI environment, you can mock a View object, and you can completely test the correctness of the Presenter business logic during the unit test sex.
* shortcoming
    * With continuous development and adding features, the code of Presenter will become more and more bloated

## MVVM

* Whether it is MVC or MVP, it is impossible to avoid the problem that the code of the Presenter (Controller) will become more and more bloated. If the same effect (external behavior) can be achieved, the less code the better (internal behavior), so MVVM was born
* Connect V, M skillfully through **ViewModel**

... unfinished

## Reference
[23 Design Patterns](https://jasonblog.github.io/note/design_pattern/index.html)
[Design Patterns in Python](https://python-web-guide.readthedocs.io/zh/latest/design/design.html)
[Python Common Design Patterns](https://refactoringguru.cn/design-patterns/python)
[MVC, MVP, MVVM](https://ihelp.ithome.com.tw/articles/10218263)
