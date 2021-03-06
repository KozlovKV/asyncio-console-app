# asyncio-console-app
Консольное приложение на python с использованием библиотеки asyncio

## Исходное техзадание
Реализовать клиент-серверное приложение на Python 3 на библиотеке asyncio:
- В двух .py файлах должны размещаться клиент и сервер – по отдельности.
- Запуск происходит через консоль. 
- Клиент должен иметь возможность отправлять данные на сервер в формате строки: "`put cpu 10.4 56161786`", "`get tyew`" и "`get *`" (`put` и `get` являются командами для сервера для записи и выдачи данных соответсвенно).
  - В примере строки `cpu` и `tyew` являются ключами по которым происходит запись и поиск информации. 
  - `10.4` - это значение переменной значения (может принимать значение только дробных цифр), а `56161786` - это метка времени (в данном задании она берется случайным образом, но всегда является целочисленным значением). 
  - `*` - это ключ для возвращения пользователю всех данных по всем ключам от сервера. 
  - По одному ключу может храниться несколько пар переменной значения и метки времени.
- Данные на сервере хранятся в виде словаря. 
- Сервер многопоточно (связь не должна прерываться) должен принимать команды от пользователей. 
  - Данные от пользователя могут быть введены не корректно – программа не должна вылетать из-за этого. 
  - На самом сервере должны быть записаны только корректные данные.
  - При удачном принятии данных сервером должны выводится для клиента слова `ок\n` при ошибке - `\nerror\nerror command\n\n`.
### Пример сервера
```python
> put mmm 11.0 628930 
< ок
< 
> get yg
< error
< error command
< 
> get *
< mmm 11.0 628930
< 
> got *
< error
< error command
< 
> put mmm 0.0 555444 
< ок
< 
> put mmm 54.9 555444 
< ок
< 
> get mmm
< mmm 11.0 628930 
< mmm 0.0 555444
< 
```