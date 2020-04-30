import csv
import os
import random as r

def suggest_book(book_list):
    rand_list = book_list.copy()
    r.shuffle(rand_list)

    return rand_list[0]


with open('/home/oguz/Documents/projects/book_suggest/books.csv') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','))

"""
item[0] -> name
item[1] -> author
item[2] -> publisher
item[3] -> genre
item[4] -> read?
"""
csv_reader = csv_reader[1:]

read = "Evet"
son_tur = "Fantastik"

while (read == "Evet"):
    suggestion = suggest_book(csv_reader)

    if (suggestion[4]=="Evet"):
        pass
    elif (suggestion[3]==son_tur):
        pass
    else:
        read = "Hayır"

print("Seçilen Kitap:", suggestion[1],"'den/dan", suggestion[0], ", Tür: ", suggestion[3])

