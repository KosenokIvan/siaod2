# Лабораторная работа №2
Косенок Иван БСТ2201
## Стек (stack):
Операции для стека: инициализация, проверка на пустоту, добавление нового элемента в начало, извлечение элемента из начала;
<br><br>
Реализован в файле *stack.py*

## Дек (двусторонняя очередь, deque):
Операции для дека: инициализация, проверка на пустоту, добавление нового элемента в начало, добавление нового элемента в конец, извлечение элемента из начала, извлечение элемента из конца.
<br><br>
Реализован в файле *deque.py*

## Задание №1
Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков
* Реализован в файле *1.py* <br>
* Входные данные: *books.txt*<br>
* Выходные данные: *result1.txt*

## Задание №2
Дек содержит последовательность символов для шифровки сообщений. Дан текстовый файл, содержащий зашифрованное сообщение. Пользуясь деком, расшифровать текст. Известно, что при
шифровке каждый символ сообщения заменялся следующим за ним в деке по часовой стрелке через один.
* Реализован в файле *2.py* <br>
* Зашифровка исходного сообщения: *encrypt.py*
* Исходное сообщение: *message2.txt*
* Входные данные (зашифрованное сообщение): *encrypted_msg2.txt*
* Выходные данные: *result2.txt*

## Задание №3
Даны три стержня и n дисков различного размера. Диски можно надевать на стержни, образуя из них башни. Перенести n дисков со стержня А на стержень С, сохранив их первоначальный
порядок. При переносе дисков необходимо соблюдать следующие правила:
1. на каждом шаге со стержня на стержень переносить только один диск;
2. диск нельзя помещать на диск меньшего размера;
3. для промежуточного хранения можно использовать стержень В. Реализовать алгоритм, используя три стека вместо стержней А, В, С. Информация о дисках хранится в исходном файле
* Реализован в файле *3.py*
* Входные данные (размеры дисков, размещающихся на 1 стержне): *hanoi3.txt*
* Выходные данные (итоговое расположение дисков - все на 3 стержне): *result3.txt*

## Задание №4
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс круглых скобок в тексте, используя стек.
* Реализован в файле *4.py*
* Входные данные: *input4.txt*
* Выходные данные: *result4.txt*

## Задание №5
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс квадратных скобок в тексте, используя дек
* Реализован в файле *5.py*
* Входные данные: *input5.txt*
* Выходные данные: *result5.txt*

## Задание №6
Дан файл из символов. Используя стек, за один просмотр файла напечатать сначала все цифры, затем все буквы, и, наконец, все остальные символы, сохраняя исходный порядок в каждой группе
символов.
* Реализован в файле *6.py*
* Входные данные: *input6.txt*
* Выходные данные: *result6.txt*

## Задание №7
Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа, затем все положительные числа, сохраняя исходный порядок в каждой группе.
* Реализован в файле *7.py*
* Входные данные: *input7.txt*
* Выходные данные: *result7.txt*

## Задание №8
Дан текстовый файл. Используя стек, сформировать новый текстовый файл, содержащий строки исходного файла, записанные в обратном порядке: первая строка становится последней, вторая –
предпоследней и т.д.
* Реализован в файле *8.py*
* Входные данные: *input8.txt*
* Выходные данные: *result8.txt*

## Вывод
В ходе выполнения работы были изучены типы данных стек и дек, 
а также реализация некоторых алгоритмов с их помощью
