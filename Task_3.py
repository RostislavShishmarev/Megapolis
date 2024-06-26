import csv


def get_books_by_author(author):
    """
    Function to get books by author or list of authors (separated by ", ")
    :param author: author of the books
    :return: list of strings with information or list with message if author is not in library
    """
    with open('books.txt', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]  # Cut headers
    # Rows format: 0 - id, 1 - isbn, 2 - authors, 3 - year, 4 - title, 5 - rating

    result = []
    for row in data:
        authors = set(row[2].split(', '))
        need_authors = set(author.split(', '))
        if authors & need_authors == need_authors:
            result.append(f'{row[4]} - {row[1]} - {row[0]} - {row[5]}')
    if result:
        return result
    return ['Данного автора в этой библиотеке нет', ]


if __name__ == '__main__':
    while True:
        input_ = input()
        if input_ == 'автор':
            break

        print(*get_books_by_author(input_), sep='\n')
