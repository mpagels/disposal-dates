import logging

def get_fallback_data(filename):
    logging.info(f"get fallback ics download - {filename}") 
    stream = open(filename, encoding='utf-8')
    ics = stream.read()
    stream.close()
    return ics

def save_file_for_fallback_use(text, filename):
    with open(filename, "w", encoding='utf-8') as ics:
        logging.info(f"write ics file - {filename}")   
        ics.write(text)