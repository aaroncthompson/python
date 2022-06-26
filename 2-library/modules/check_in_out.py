# put functions relevant to check in / out here

def library_formatting(title, author, year, medium, item_id, qty):
    new_book = {}
    new_book['title'] = title
    new_book['author'] = author
    new_book['year'] = year
    new_book['medium'] = medium
    new_book['id'] = item_id
    new_book['qty'] = qty
    return new_book
