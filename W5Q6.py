def remove_indentation(text):
    return '\n'.join([line.lstrip() for line in text.splitlines()])

text = """    This is a text
        with indentation.
    It has several lines."""
print(remove_indentation(text))
