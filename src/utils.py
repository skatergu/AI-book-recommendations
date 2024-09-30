# Helper functions for sorting and other utility functions can go here.


def sort_books(books, sort_by, order='asc'):
    reverse = order == 'desc'
    return sorted(books, key=lambda x: x[sort_by], reverse=reverse)
