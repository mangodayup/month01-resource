"""
    函数参数
        形式参数
            双星号字典形参
"""
# 关键字实参数量无限
def func01(**kwargs):
    print(kwargs) # {'a': 1, 'b': 2}

func01(a=1,b=2)
# func01(1,2,3)
