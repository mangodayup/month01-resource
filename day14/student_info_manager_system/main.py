from usl import StudentView

# 如果不是主模块,当前代码不执行
if __name__ == '__main__':
    # 主模块(第一次执行的入口代码)
    # 不会生成pyc文件
    # 只有被导入的模块才会自动生成pyc文件
    view = StudentView()
    view.main()
