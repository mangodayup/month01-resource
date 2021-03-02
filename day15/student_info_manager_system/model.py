class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name  # type:str
        self.age = age  # type:int
        self.score = score  # type:int
        # 唯一标识数据的编号
        self.sid = sid  # type:int
