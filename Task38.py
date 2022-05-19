#38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "ываабв лповап абвцукв алоабвабв ываываыв 325валлвы 590957907абв34235233454590787"
sep = ' '
result = [x+sep for x in text.split(sep)]
print('Исходный текст =')
print(text)
a = input('Введите кобцинацию символов содержащихся в словах, для последующего удаления этих слов \n')
b = len(result)
ind = 0
textout = []

while ind < b:
    if a in result[ind]:
        textout = textout
    else:
        textout.append(result[ind])
    ind = ind + 1

print('Текст после редакции -')
print(" ".join(map(str, textout)))