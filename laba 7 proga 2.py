"""б) Задача. Вивести дані про книги, в яких кількість сторінок більше 150. Поля
структури: Автор, Кількість сторінок, Тираж, Рік видання."""

Info = {
    "Perevtilenia": {"Author": "Kafka", 'Pages': 183,
                     'turazh': 3513, 'Year of realize': 1876
                     },
    "Harry Potter":{'Author':'Rouling', 'Pages':213,
                    'turazh':3241,'Year of realize':1834
                    },
    'Misto':{'Author':'Unknown', 'Pages':82,
             'turazh':23423,'Year of realize':1658}
}
books = ['Perevtilenia','Harry Potter','Misto']
for book in books:
    Pages = Info[book]['Pages']
    if Pages > 150:
        print(book,Info[book]['Pages'])