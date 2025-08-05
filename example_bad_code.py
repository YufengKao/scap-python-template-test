# 这是一个包含各种代码风格问题的示例文件

def bad_function( x ):
    """这是一个有问题的函数"""
    unused_var = 42
    lst = [1,2,3,4,5]
    for i in range(len(lst)):
        print(lst[i])
    return x

class BadClass:
    def __init__(self):
        pass

    def method(self,param):
        if param==None:
            return True
        return False

# 未使用的导入

# 行尾有多余空格
def another_function():
    pass
