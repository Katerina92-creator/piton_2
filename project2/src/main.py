"""Лекция 2."""
from module import hello
hello()
print("___пункт 1___")
class EmptyClass:
   """Класс клиент."""
   def __init__():
      """Конструктор."""
      pass
      
   def meth():
      """_Когда то что то будет делать_."""
      ...
def todo():
   print("Готово")

todo()

print("___пункт 2___")
name=input("введите имя ") 
age=input("введте возраст ")
print(f"Привет, {name}, через 5 лет тебе будет  {int(age) + 5} лет")  

print("___пункт 3___")
if True:
   print("Hello")

print("___пункт 4___")
number=int(input("введте число "))
if number > 0:
   print("positive")
elif number < 0:
   print("negative")
else:
   print("zero")   

print("___пункт 5___")
range_list = [10, 20]
if (range_list[0]<= number <= range_list[1]):
#if (number <= 20 and number >=10):
   print(f"число {number} входит в диапазон от 10 до 20")
else:
   print(f"число {number} не входит в диапазон от 10 до 20")   
if number is None:
   print(f"число {number} не определно")   

print("___пункт 6___")

stroka_inp=input("введте start stop или pause ")
match stroka_inp:
   case "start":
      print("запуск")
   case "stop":
      print("остановка")
   case "pause":
      print("пауза")
   case _:
      print("Неизвестная команда") 

print("___пункт 7___")
items=[1,2,3,4,5]
for idx in items:
   print(idx * idx)

psw_inp=""
while psw_inp != "1234":
   psw_inp=input("введте пароль 1234 ")
else:
   print("успешный вход") 

print("___пункт 8___")
inp_num=input("введте число для деления на 10 ")
try:
   inp_num/10
except TypeError as v:
   if isinstance(inp_num, str):
      print("введена строка")
except ValueError as e:
   if inp_num==0:
      print("введен 0")
finally:
   print("Программа завершена")         


print("___пункт 10___")
#тернарный оператор
res = 'even' if number % 2 ==0 else 'odd'
print(res)
#моржовый оператор
stroka_input=input("введте число или что-то другое ")
if stroka_input.isdigit():
   print("это число")
else:
   print("это не число")
