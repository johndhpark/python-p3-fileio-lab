def write_file(file_name, file_content):
    opened_file = open(f'{file_name}.txt', mode='w', encoding='utf-8');
    opened_file.write(file_content)

def append_file(file_name, append_content):
    opened_file = open(f'{file_name}.txt', mode='a', encoding='utf-8');
    opened_file.write(append_content)

def read_file(file_name):
    opened_file = open(f'{file_name}.txt')
    return opened_file.read()
