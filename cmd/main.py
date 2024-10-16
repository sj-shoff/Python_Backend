class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.marks = [5, 3, 5]

    # Dunder или magic методы - методы с двумя _ в начале и в конце
    # Эти методы обладают "магическими" свойствами

    # __str__ - применяется к обьекту при вызове str от него, например, при принте этого объекта
    def __str__(self) -> str:
        return f"{self.name}, {self.age} лет"


yaroslav = Student("Yaroslav", 18)

print(yaroslav)