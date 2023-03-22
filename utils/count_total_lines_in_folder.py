import os

def is_file(string):
    try:
        file = open(string,"r")
        file.close()
        return True
    except Exception as e:
        return False

def get_all_file_in_folder(path):
    all_content = os.listdir(path)
    files = []
    for content in all_content:
        if is_file(content):
            files.append(content)
    return files


def count_lines_in_file(filename) -> int:
    file = open(filename,'r')
    count = len(file.readlines())
    file.close()
    return count

def count_lines_in_folder():
    all_files = get_all_file_in_folder(os.getcwd())
    count = 0
    for file in all_files:
        count += count_lines_in_file(file)
    return count

if __name__ == "__main__":
    print(count_lines_in_folder())

