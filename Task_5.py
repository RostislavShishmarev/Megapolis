import csv


def create_books_dict():
    """
    Function to get dict of dicts with information about books
    Format:
    {
      book ISBN: {
          'author': list of authors
          'title': book title
          'date': int number of publication year
          'rating': float number of rating
      }
    }
    :return: list of dicts
    """
    with open('books.txt', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]

    result = {}
    for row in data:
        result[row[1]] = {
            'authors': row[2].split(', '),
            'title': row[4],
            'date': int(row[3]),
            'rating': float(row[5].replace(',', '.')),
        }
    return result


def get_books_by_year(year):
    """
    Function to get books by year
    :param year: publication year
    :return: list of book dicts; format:
    {
      'author': list of authors
      'title': book title
      'date': int number of publication year
      'rating': float number of rating
    }
    """
    books = create_books_dict()
    result = []
    for isbn, book in books.items():
        if book['date'] == year:
            result.append(book)
    return result


def print_best_books_for_years(years):
    """
    Function to print best book for each year;
    If no books in year, function skip it
    :param years: iterable of years
    :return: None
    """
    for year in years:
        books = get_books_by_year(year)
        if not books:
            continue
        print(f'Год: {year}')
        best_book = max(books, key=lambda book: book['rating'])
        print(f"{best_book['title']} {best_book['rating']}")


if __name__ == '__main__':
    print_best_books_for_years(range(2000, 2007 + 1))
