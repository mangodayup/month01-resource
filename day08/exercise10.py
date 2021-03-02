"""
    画出下列代码内存图
"""
data01 = 10
def func01():
    data02 = 10
    global data01
    data01 += 5
    data02 += 5
    print(data01)
    print(data02)
func01()
func01()
