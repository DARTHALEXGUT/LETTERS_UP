from Letters import alph  # Подключаем алфавит
str = input('')
str = str.lower()
output = ''
string_length = len(str)

for a in range(7):  # вывод в консоль
    for  b in range(string_length):
        for i in range(0 + 9 * a, 8 + 9 * a):
            output = output + alph[str[b]][i]
    print(output)
    output = ''

f = open('Out.txt', 'w')
for a in range(7):  # вывод в файл
    for b in range(string_length):
        for i in range(0 + 9 * a, 8 + 9 * a):
            output = output + alph[str[b]][i]
    f.write(output + '\n')
    output = ''
f.close()
