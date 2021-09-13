def print_book_info(title, author=None, year=None):
    #  Write your code here
    message = f'"{title}"'
    if author is not None or year is not None:
        message = f"{message} was written"
    if author is not None:
        message = f"{message} by {author}"
    if year is not None:
        message = f"{message} in {year}"
    print(message)
