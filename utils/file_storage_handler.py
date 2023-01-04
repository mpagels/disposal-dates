def get_fallback_data(filename):
    stream = open(filename, encoding='utf-8')
    ics = stream.read()
    stream.close()
    return ics

def save_file_for_fallback_use(text, filename):
    with open(filename, "w", encoding='utf-8') as ics:
        ics.write(text)