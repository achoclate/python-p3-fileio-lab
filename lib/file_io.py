# lib/file_io.py

def write_file(file_name, file_content):
    # Add .txt extension to file name
    file_name = f'{file_name}.txt'
    with open(file_name, 'w') as f:
        f.write(file_content)

def append_file(file_name, file_content):
    # Add .txt extension to file name
    file_name = f'{file_name}.txt'
    with open(file_name, 'a') as f:
        f.write(file_content)

def read_file(file_name):
    # Add .txt extension to file name
    file_name = f'{file_name}.txt'
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
