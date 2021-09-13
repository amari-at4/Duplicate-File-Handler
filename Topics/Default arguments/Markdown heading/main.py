def heading(title, level=1):
    if level < 1:
        level = 1
    elif level > 6:
        level = 6
    return '{} {}'.format('#' * level, title)

