import io
#все комбинации двух букв собираем в одном списке
def bigram(alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
    b = []
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if b.count(alphabet[i]+alphabet[j]) == 0:
                b.append(alphabet[i]+alphabet[j])
    return b
#все комбинации трех букв собираем в одном списке
def trigram(alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
    b = []
    c = bigram()
    for i in range(len(alphabet)):
        for j in c:
            if b.count(alphabet[i]+j) == 0:
                b.append(alphabet[i]+j)
    return b
def analiz_na_chastoty(text):
    text = text.lower()

    print("Какой частотный анализ вам нужен?")
    print("a. Частотный анализ букв")
    print("b. Биграмма")
    print("c. Триграмма")

    a = input()
    b = {}
    file = ''

    if a == 'a':
        file = "Analiz_na_chastotu.txt"
        for i in range(len(text)):
            b[text[i]] = text.count(text[i])
    elif a == 'b':
        file = "Analiz_na_chastoty_bigramma.txt"
        k = bigram()
        for i in range(len(text)):
            for j in k:
                if text.count(j) > 0:
                    b[j] = text.count(j)
    elif a == 'c':
        file = "Analiz_na_chastoty_trigramma.txt"
        k = trigram()
        for i in range(len(text)):
            for j in k:
                if text.count(j) > 0:
                    b[j] = text.count(j)
    else:
        print("Данный анализ не оступен!")

    sum = 0

    for i in b:
        sum += b[i]
    for i in b:
        b[i] = (b[i] / sum) * 100

    with io.open(file, 'w', encoding="utf-8") as file_object:
        file_object.write("Частотный анализ букв")
        for j in b:
            file_object.write(f"\n<{j}> = {str(b[j])}%")
    return b

print("Добро пожаловать!")
text = """Масса не пропорциональна объёму.

Девушка, порхающая, как лепесток по вéтру,
Эта девушка, словно нежная фиалка,
Притягивала меня сильнее притяжения планеты.

Мгновение.
Я превратился в яблоко Ньютона,
Что упало к её ногам в забвении.

Удар.
Удар и ещё удар.
Моё сердце качалось, как маятник,
Падая с небес, в плену её чар.

Это была первая любовь."""
analiz_na_chastoty(text)
# import re
# def izmenenie_text(text):
#     a = re.sub(r'[^\w\s]', '', text.lower()).split()
#     return a