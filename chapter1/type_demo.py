class CachedMate(type):
    """
    作用跟type一样，就是用来创建 class 的
    """

    def __new__(mcs, clsname, bases, attrs):
        """
        type 的 __new__ 方法作用是根据 类名clsname、依赖bases、属性attrs 这些字面量来创建出一个类
        就像普通 class 中定义的 __new__ 方法作用是创建一个 object
        metaclass 中定义的 __new__ 方法作用是创建一个 class
        返回的 new_class 就是被创建出来的类
        """
        print(f'CachedMate __new__ start {clsname} || {bases} || {attrs}')
        new_class = super().__new__(mcs, clsname, bases, attrs)
        print(f'CachedMate __new__ gen class {new_class} || {type(new_class)} || {type(type(new_class))}')
        print(f'CachedMate __new__ end')
        print('======')
        return new_class

    def __init__(cls, clsname, bases, attrs):
        """
        给创建出来的 class 做一些初始化操作
        就像普通 class 中定义的 __init__ 方法作用是给创建的 object 初始化
        metaclass 中定义的 __init__ 方法作用是给创建的 class 初始化
        """
        print(f'CachedMate __init__ start {clsname} {bases} {attrs}')
        obj = super().__init__(clsname, bases, attrs)
        print(f'CachedMate __init__ gen obj {obj} {type(obj)} {type(type(obj))}')
        print(f'CachedMate __init__ end')
        print('======')

        # self.__cache = weakref.WeakValueDictionary()
        cls._cache = {}

    def __call__(cls, *args, **kwargs):
        """
        继续类比普通class中的场景
        对象object以调用方式出现时，就是在调用class中定义的 __call__，如object()
        而类class以调用方式出现时，就是在调用metaclass中定义的 __call__，如class()
        这里就是当Spam()时，也就是实例化Spam时就会调用

        这也就是为什么单例模式可以放在这里做的原因，目标类实例化时，必然会调用 __call__ 所以固定返回同一个实例，即实现单例
        或者说，想要控制一个类的创建过程，都可以在这里坐处理
        """
        print(f'CachedMate __call__ start', args, kwargs)

        if args in cls._cache:
            print('CachedMate __call__ cached')
            return cls._cache[args]
        else:
            print('CachedMate __call__ before super().__call__')
            obj = super().__call__(*args, **kwargs)
            print('CachedMate __call__ after super().__call__', obj, type(obj))
            cls._cache[args] = obj
            return obj

# Example
class Spam(metaclass=CachedMate):
    def __new__(cls, *args, **kwargs):
        print('Spam __new__', args, kwargs)
        return super(Spam, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Spam __init__', args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        # 在Spam实例上使用 spam() 才会调用这里
        print('Spam __call__', args, kwargs)

# 结果中Spam实例化参数不变，得到的就是缓存的结果，参数变了则是新接口
print(11111, Spam._cache)
# 11111 {} 一开始没有缓存

sp = Spam(1,2,'test1', 'test2', name='test_name')
print(22222, Spam._cache)
# 22222 {(1, 2, 'test1', 'test2'): <__main__.Spam object at 0x10b71b160>}
# 有了一个缓存

sp2 = Spam(1,2,'test1', 'test2', name='test_name')
print(33333, Spam._cache)
# 33333 {(1, 2, 'test1', 'test2'): <__main__.Spam object at 0x10b71b160>}
# 因为参数一样，所以读的缓存

sp3 = Spam(1,2,'test1', 'test3', name='test_name3')
print(44444, Spam._cache)
# 44444 {(1, 2, 'test1', 'test2'): <__main__.Spam object at 0x10b71b160>, (1, 2, 'test1', 'test3'): <__main__.Spam object at 0x10b71b250>}
# 参数变了，重新生成了新的缓存，独立开来
