import csv

if __name__ == '__main__':
    with open('books.txt', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]

    ratings_dict = {}
    for row in data:
        authors, rating = row[2].split(', '), float(row[5].replace(',', '.'))
        for author in authors:
            ratings_dict[author] = ratings_dict.get(author, []) + [rating]

    result_data = [['authors', 'ratings_authors'], ]
    for author, ratings in ratings_dict.items():
        result_data.append([author, round(sum(ratings) / len(ratings), 2)])

    with open('books_new.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='%')
        writer.writerows(result_data)

    # Min by (rating, author name)
    worst_writer, rating = min(result_data[1:], key=lambda row: (row[1], row[0]))
    print(f'{worst_writer} - {rating}')
