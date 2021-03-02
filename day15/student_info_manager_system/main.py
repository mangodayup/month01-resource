from usl import StudentView

if __name__ == '__main__':
    # 全局异常处理
    try:
        view = StudentView()
        view.main()
    except:
        print("出错了")
