""" классы """
class Student:
    """Класс студент."""
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def __str__(self):
        return f'Студент {self.name}, возраст {self._age}'
        
    def __repr__(self):
        return self.__str__()    

    def get_info(self):
        return f"Студент {self.name}, возраст {self._age}"

class GraduateStudent(Student):
    """Класс аспирант наследник класса Student"""
    def __init__(self, name, age, research_topic):
        super().__init__(name, age)
        self._research_topic = research_topic
        self.__publications = 0

    def __str__(self):
        return f'Студент {self.name}, возраст {self._age}, кол-во публ {self.__publications}, тема {self._research_topic}'
        
    def __repr__(self):
        return self.__str__()    

    def add_publication(self):
        self.__publications = self.__publications + 1

    def print_publ(self):
        print(f"колличество публикаций: {self.__publications}")

    def get_info(self):
        return super().get_info() + f" тема: {self._research_topic}"

class StudentManager():
    """Класс для работы с коллекцией студентов"""
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]
    def print_all_info(self):
        indx = 0
        print("Итоговый вывод по всем студентам:")
        for i in self.students:
            indx += 1
            print(indx, ":", i)
#main
student1 = Student("Анна", 20)
print(student1.get_info())

grad_student = GraduateStudent("Петр", 25, "Искусственный интеллект")
print(grad_student.get_info())  

grad_student.add_publication()
grad_student.add_publication()
grad_student.print_publ()

manager = StudentManager()
manager.add_student(student1)
manager.add_student(grad_student)

print("кол-во студентов:", len(manager))
print("вывод студента по индексу:")
print(manager[1])

manager.print_all_info()