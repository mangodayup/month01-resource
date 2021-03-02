"""

"""


class XXModel:
    def __init__(self, data01=0, data02=""):
        self.data01 = data01
        self.data02 = data02

class XXView:
    def __init__(self):
        self.__controller = XXController()

    def func01(self):
        model = XXModel(10, "p")
        self.__controller.func02(model)

class XXController:
    def func02(self, model):
        print(model.__dict__)

view = XXView()
view.func01()
