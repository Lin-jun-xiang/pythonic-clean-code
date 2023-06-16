# Design Pattern
[中文版](README.zh-TW.md) | [English](README.md)

* 設計模式是一組重複使用的代碼設計經驗的總結,為大多數人所知,編目編碼.
* 使用設計模式是為了代碼的複用,讓代碼更容易被別人理解,保證代碼的可靠性.
* 接口=接口,對象=對象
* 預知:面向對象、類別與對象、可變與不可變對象、賦值傳遞、Decorator. [參考概念]()


* 大綱:
    * 基本供稿
        * [面向對象和設計模式簡介](#introduction)
            * [面向對象的大綱](#intro-oop)
            * [設計模式簡介](#intro-design-pattern)
        * [繼承]()
        * [抽像類、接口](#abstractorinterface)
        * [多類型]()
        * [封裝](#encapsulation)
    * [23種設計模式](https://jasonblog.github.io/note/design_pattern/index.html)
     : emoji_heavy_check_mark: 常用
        * **創意模式**
            * [單例](#singleton)
            * [抽象工廠](#)
            * [建造者](#)
            * [工廠方法](#)
            * [原型](#)
        * **結構模式**
            * [適配器](#)
            * [橋](#)
            * [複合](#)
            * [裝飾器](#decorator):heavy_check_mark:
            * [外觀](#)
            * [享元](#)
            * [代理](#)
        * **行為模式**
            * [模板方法](#)
            * [命令](#)
            * [解釋器](#)
            * [中介](#)
            * [迭代器](#)
            * [觀察者](#)
            * [責任鏈](#)
            * [紀念品](#)
            * [狀態](#)
            * [策略](#strategy):heavy_check_mark:
            * [訪客](#)
    * 特殊設計
        * [MVC(從 Observer、Strategy、Composite 演變而來)](#mvc):heavy_check_mark:
        * [MVP](#mvp):heavy_check_mark:
        * [MVVM](#mvvm):heavy_check_mark:
    * [參考](#reference)


## Introduction

#### Intro-OOP

基本原理(1~5又稱SOLID)

* **單一職責原則(SRP:Single Responsibility Principle)** 一個類別應該只有一個改變的原因
* **開、閉原則(OCP:Open Closed Principle)**對擴展開放(open for extension)和對修改關閉(closed for modification)
* **里氏替換原則(LSP:Liskov Substitution Principle)** 子類別必須能夠替換父類別.
* **接口隔離原則(ISP:Interface Segregation Principle)**
* **依賴倒置原則(DIP:Dependency Inversion Principle)** Abstraction should not depend on details, details should depend on abstraction. 因為圖像比較穩定. 高層模塊不應該依賴低層模塊,兩者都應該依賴於抽象. 程序到接口,而不是具體實現.
* **得墨忒耳法則(LoD:Law of Demeter)** 最少知識原則 只與你最親密的朋友交談

     例如:郵遞員寄掛號信,收件人需要蓋章. 一般人不會讓郵遞員自己進屋找章,既浪費時間又浪費時間不安全. 一般都是自己進屋拿,或者讓其他家人幫我拿. 因為不應該給郵遞員進屋找東西的權限,而且郵遞員不需要知道印章放在房子的什麼地方.
* **Composition/Aggregation Reuse Principle (CARP)(複合/聚合重用原則)**使用更多的合成/聚合和更少的繼承. 當兩個對像有一個has-a(has-parts,is-part-of) relationship => composition/aggregation (A has a B) 當兩個對像有 is-a (is-a-kind-of) 關係時 => 繼承 (Superman is a kind of Person)
    * Composite(複合): 當兩個對象A和B有復合關係時,表示其中一個對象消失了(ex:book),另一個對像也消失了(ex:chapter).
    * Aggregate(聚合):當A和B兩個對象存在聚合關係時,表示其中一個對象消失了(ex:team),另一個對像沒有消失(ex:player)%_ddot_ %

<a href="#top">Back to top</a>

#### Intro-Design Pattern

* 創作模式
    * **簡單工廠模式** 使用類的靜態方法根據不同的條件獲取不同的對象,使用獲取到的對像做類似的事情. 缺點是當你想添加不同的條件時,你必須修改類別的靜態方法.
    * **工廠方法模式(Factory Method Pattern)**避免了簡單工廠模式.在添加條件的時候,修改工廠類的靜態方法(修改要關閉).
    * **抽象工廠模式(Abstract Factory Pattern)** 抽象工廠類別,可以返回相同類型的工廠. 這些返回工廠,有多個相同的方法,做類似的事情.
    * **建造者模式(Builder Pattern)**梳理了某類產品構建過程的生產步驟,所有想要生產該類產品的類都必須實現這些標準化的步驟. 另外,為了避免在實際製作過程中漏掉某個步驟,一系列的製作步驟由一個指揮官類完成.
    * **原型模式(Prototype Pattern)** 複製一個已有對像生成新對象. 淺克隆: 只複製舊對象的屬性,不復制舊對像中的對象. 所以新舊對象會共享這些其他對象. 深度克隆:舊對象和其他引用對像中的屬性會被複製.
    * **Singleton Pattern** 允許一個類別只有一個實例(Instance)方法 . 生成單個實例的方式: Lazy initialization:實例只在第一次使用時生成. Eager initialization:類加載時生成一個實例,不管後面是否會用到.

* 結構模式
    * **Adapter Pattern** 一個已有的類,接口不是用戶期望的 . 適配器作為中間接口,提供用戶期望的接口. 可以分為兩種實現方法對象適配器模式(Object Adapter Pattern):將已有的類實例包裝在適配器類中. Class Adapter Pattern(類適配器模式):使用多重繼承.
    * **橋接模式(Bridge Pattern)**把一個對象的具體行為(實現)抽取出來,成為一個獨立的對象. 即原來的一個對像變成了兩個對象:“抽像對象”+“真實對象” object". 優點是抽像對象和真實對象可以解耦,獨立變化.
    * **Composite Pattern** 幾個對象之間,有一個樹結構.
    * **裝飾器模式(Decorator Pattern)**動態給一個對象添加函數.函數是一層層應用的,每一層實現不同的對象.
    * **Facade Pattern** 把原來的大系統打包,用另一個更簡單的接口開放給用戶. 用戶只需要知道接口的使用方法就可以了. 不需要了解的運行方式大系統中的各個小系統.
    * **享元模式** 對象之間,如果存在可以共享的公共部分,則將可共享部分分離為共享對象,將不可共享部分外化,然後使用外化部分傳遞to shared objects. 這樣的好處是減少內存佔用. 缺點是程序邏輯可能會變得比較複雜.
    * **代理模式(Proxy Pattern)**有兩個對象,代理對象和真實對象.系統使用代理對象進行操作,真實對像在代理對象內部進行操作%_ddot_ % 應用:遠程代理、虛擬代理、安全代理

* 行為模式
    * **Chain-of-responsibility Pattern** 有幾個對象可以處理某個請求,但是處理的範圍(權限)不同. 當這個對像沒有處理權限時,可以通過此請求到下一個對象繼續處理.
    * **命令模式(Command Pattern)** 一般的命令包括發出命令和執行命令 . 命令模式就是把這個過程拆分成三個對象,發出命令的對象(Invoker),執行命令的對象執行命令(command),執行命令的對象(receiver). Invoker對像用於構建要執行的命令. 這樣,當需要擴展功能時,比如添加重複執行命令,取消命令...,等.,變得更簡單.
    * **解釋器模式(Interpreter Pattern)**用於解釋和翻譯一種語言.
    * **迭代器模式(Iterator Pattern)**一種遍歷容器中元素的方法.
    * **中介者模式** 當對象之間可能存在錯綜複雜的交互時,可以將這些關係交給另一個對象(中介者)來降低這些對象之間的交互耦合.
    * **備忘錄模式(Memento Pattern)** 一種將對象恢復到之前狀態的方法.
    * **觀察者模式(Publish/Subscribe Mode)(觀察者模式)**兩種類型的對象,“通知者”和“觀察者”.
        * 訂閱:“通知者”可以在訂閱列表中添加或刪除“觀察者”
        * 發布:當需要監聽的事件發生時,“通知者”可以從訂閱列表中通知“觀察者”該事件,“觀察者”會對事件採取相應的動作.
        * 作用:解耦,讓耦合的兩邊依賴於抽象(接口)而不是具體的.
    * **狀態模式(State Pattern)**一個對像有多個狀態,在不同的狀態下有不同的行為.一般情況下可能會用多個if else來處理這些分支行為.如果狀態模式被使用,這些狀態被處理並提取到另一個類來處理這些分支. 也就是if else被重寫為一個類.
    * **Strategy Pattern** 將不同的算法定義為一個家族.這些算法實現了相同的接口,並作為單獨的類別來編寫,因此它們可以相互替換. 優點是如果你想添加以後有新的算法,只需要在原來的類別不移動的情況下,多加一個類別.
    * **Template Method Pattern** 將不變的部分移到父類中,去掉子類中重複的代碼
    * **訪問者模式(Visitor Pattern)** 當一個“對象結構”中的“元素”幾乎沒有變化,但這些“元素的行為”經常增加或減少時,訪問者模式適用於. visitor mode是提取“元素的行為”,將每個行為做成一個“Visitor(訪問者)對象”. 每個“Visitor(訪問者)對象”都可以與原來的“對象結構”不同.”產生不同行為的元素”.

<a href="#top">Back to top</a>

## Abstractor、Interface

python與java相比,嚴格區分抽象和接口. Python沒有原生的抽像類和方法,必須使用abc包來實現抽像類和接口. 在Python中不管是抽像類還是接口, 它繼承了 abc.ABC.
(`C:\//Users\//junxianglin\//AppData\//Local\//Programs\//Python\//Python38\//lib\//abc.py`)

* 抽像類(abstractor)
     * 類的抽象
    * **無法具體化的類別**
    * 當一個方法(Method)被`@abc.abstractmethod`裝飾器(decorator)覆蓋時,意味著抽象方法的建立必須依賴子類override.

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

* 接口/接口(接口)
     * 行為的抽象

* 抽象基類(abstractor basic class,abc)
     假設我們要開發一個數據接口,有三個功能:連接數據庫、讀取數據、執行SQL. 這些功能可以先通過ABC定義,然後由子類負責實現(重寫)
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

* 封裝的目的是防止外界有任何機會以意想不到的方式改變對象. 封裝可以加強對象的健壯性.
* python中有一個`property`裝飾器,可以把一個方法變成一個屬性,相當於封裝了這個屬性. 外界不需要知道獲取這個屬性的實現方法,也不會隨意更改.

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

* 單例

## Decorator

* 裝飾者模式(Decorator)
* 專注於在“**不修改原有對像或功能**”的前提下動態地為對象“**添加新功能**”
* 何時使用:**多個功能需要做一些前置或後置工作**,可以統一裝飾,比如日誌驗證
* 特徵:
    * 不修改已有函數的源碼
    * 不修改已有函數的調用方式
    * 向現有功能添加額外功能
* Python 內置的新函數可以通過 `＠` 擴展到現有對象
* 常見的擴展類別有:**數據驗證(pydantic)**、**緩存**、日誌記錄、監控、**調試**、業務規則、加密、壓縮……

<details>
<summary>Timeit</summary>

* 不改變原來的對象f1
* 執行f1之前:記下時間
* 執行f1後:記錄時間,打印出f1的執行時間
* 匹配時序:多個函數需要記錄執行時間

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

* 通過緩存機制,記下計算過程,遇到重複過程**避免重複計算**(streamlit也可以使用`@cache`處理加載數據)
* 將經常重複使用的計算結果存放在存取速度較快的內存中,以加快獲取結果的方式.
* 數據量大的時候會遇到內存佔用的問題,這是一把雙刃劍

* 自定義一個簡單的緩存裝飾器,提高計算代價數組的性能. 通過緩存獲取重複的fib(i)

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

* %_內聯代碼_%
    * 基於最近最少使用(LRU)算法實現緩存功能,自動管理緩存大小(**自動刪除最少使用**)
    * maxsize 定義遞歸的深度,只需要注意

        ```python
        from functools import lru_cache

        @lru_cache(maxsize=100)
        def fib(n): 
            if n < 2: 
                return 1 
            return fib(n-1) + fib(n-2)
        ```

    * **適用於任意重複計算函數**

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

    * 修改“返回變量對象”功能,需要使用copy. [參考](https://www.zhihu.com/question/350078061)

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

* debug通常是通過`print`來輔助的,從下面的函數可以看出,我們會侵入式修改對象,最終不得不去掉print,相當不方便

    ```python
    def sum(a, b):
        print("a=", a)
        print("b=", b)
        print("a+b=", a+b)
        return a+b
    ```

* 通過調試裝飾器

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

* 多加一層裝飾器
* 在限制輸出 k 之前

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

* 多個裝飾器的執行順序

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

* 戰略模式(Strategy)

* 屬於Behavior Mode,將一組**行為轉化為對象**

* 專注於在運行時選擇不同的算法或行為, **面對不同的情況,需要做出不同的行為,即策略**
    * 排序算法有很多種,我們可以根據數據大小選擇不同的算法

* 場景:大數據系統推送文件,根據不同類型採用**不同分析**
    * 非設計模式
         缺點:代碼臃腫,調整類型時需要改回原代碼
        ```python
        if ():
            ...
        elif ():
            ...
        else ():
            ...
        ```
    * 策略模式
        * `ParserStrategy`:策略的抽象基類,每個具體的解析策略都繼承這個類定義的行為`parse`
        * `ParserContext`:解析後的上下文類,根據傳入的數據類型選擇對應的策略
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

* **文件分離**:將不同功能的代碼放在不同的文件中

    (三個文件夾:Model、View、Controller)

* 三種結構
    * 模型:負責與數據庫通信
    * View:負責管理屏幕的渲染,即HTML模板(template)
    * Controller:程序邏輯,M和V之間的橋樑 . 來自路由的請求會先發送給Controller,然後Controller通知Model調度數據,將數據傳遞給查看生成模板(template)

        <img src='img/2023-06-16-11-28-31.png' width='60%' />

* 路由器與控制器

    * Router:工作分配,將對應的URI和controller放入routes[]
    * Controller:負責工作,執行M和V之間的通信

    (開發API時,只需要專注於使用Router來分隔不同的api路由即可)

* 優勢
    * 非常直觀,容易理解
    * 使用Controller分離Model和View,有一定程度的解耦
* 缺點
    * **三者相互依賴**,一旦其中一個更新,另外兩個必須相應修改
    * 隨著不斷的開發和添加功能,**Controller代碼會越來越臃腫**
    * 很難進行單元測試

## MVP

* 為了改善MVC的缺點,用Presenter替換Controller
* 與MVC不同的是,Model層拿到數據後,不是直接傳給View更新,而是返回給Presenter,Presenter再傳數據給View,更新屏幕%_ddot_ %(從三者相互依存到兩者相互依存)

    <img src='img/2023-06-16-11-34-12.png' width='60%' />

* 優勢
    * 從三者的相互依賴到只依賴Presenter(改動的地方比較少)
    * 職責明確,分工明確
    * View只負責在收到用戶反饋後調用Presenter獲取數據,並在收到數據時更新屏幕.
    * Model被動接收Presenter命令,獲取數據,回傳給Presenter.
    * Presenter通過接口與View和Model進行通信,是View和Model之間唯一的鏈接窗口.
    * 方便單元測試
        
        因為Presenter是通過接口操作View的,所以在對不依賴UI環境的Presenter進行單元測試的時候,可以mock一個View對象,就可以完全測試Presenter的正確性單元測試期間的業務邏輯性.
* 缺點
    * 隨著不斷的開發和添加功能,Presenter的代碼會越來越臃腫

## MVVM

* 無論是MVC還是MVP,都無法避免Presenter(Controller)的代碼會越來越臃腫的問題. 如果能達到同樣的效果(外部行為),代碼越少越好(內部行為),於是MVVM誕生
* 通過**ViewModel**巧妙的連接V,M

... 未完成

## Reference
[23種設計模式](https://jasonblog.github.io/note/design_pattern/index.html)
[Python 中的設計模式](https://python-web-guide.readthedocs.io/zh/latest/design/design.html)
[Python常用設計模式](https://refactoringguru.cn/design-patterns/python)
[MVC、MVP、MVVM](https://ihelp.ithome.com.tw/articles/10218263)
