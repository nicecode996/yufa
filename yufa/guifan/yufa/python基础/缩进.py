# conding=utf-8

# 代码块的内容相当于首行缩进一个级别（4个空格），示例如下：

class abstractclassmethod(classmethod):
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable._isabstracamethod_ = True
        super().__init__(callable)


def _new_(mcls, name, bases, namespace, **kwargs):
    cls = super().__new__(mcls, name, bases, namespace, **kwargs)
    for base in bases:
        for name in getattr(base,"_abstractmethods_", set()):
            value = getattr(cls, name, None)
            if getattr(value,"_isabstractmethod_",False):
                abstracts.add(name)
    cls.abstacmethods_  = frozenset(abstracts)

    return cls
