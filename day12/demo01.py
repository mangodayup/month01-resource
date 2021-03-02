"""
    继承 - 行为
        财产:钱不用孩子挣,但是可以直接花
        编程:代码不用子类写,但是可以直接用
"""
# 多个类型有相同代码,而且在概念上是统一的.
class Person:
    def say(self):
        print("讲话")

class Student(Person):
    def play(self):
        self.say()
        print("玩耍")

class Teacher(Person):
    def teach(self):
        print("讲课")

# 父类对象只能访问父类成员
p01 = Person()
p01.say()

# 子类对象能访问父类成员也能访问子类成员
t01 = Teacher()
t01.say()
t01.teach()

# 继承相关函数
# 1. 对象 与 类型的关系判定
# 老师对象 是一种 老师类型  True
print(isinstance(t01, Teacher))
# 老师对象 是一种 人类型    True
print(isinstance(t01, Person))
# 老师对象 是一种 学生类型  False
print(isinstance(t01, Student))
# 人对象 是一种 学生类型  False
print(isinstance(p01, Student))

# 2. 类型 与 类型的关系判定
# 老师类型 是一种 老师类型  True
print(issubclass(Teacher, Teacher))
# 老师类型 是一种 人类型    True
print(issubclass(Teacher, Person))
# 老师类型 是一种 学生类型  False
print(issubclass(Teacher, Student))
# 人类型 是一种 学生类型  False
print(issubclass(Person, Student))


# 3. 对象的类型 与 类型的关系判定
# 老师对象的类型 是 老师类型  True
print(type(t01) == Teacher)
# 老师对象的类型 是 人类型    False
print(type(t01) == Person)
# 老师对象的类型 是 学生类型  False
print(type(t01) == Student)
# 人对象的类型 是 学生类型  False
print(type(p01) == Student)





