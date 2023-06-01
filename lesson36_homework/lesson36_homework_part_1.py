import functools
from cryptography.fernet import Fernet
import os
import datetime


def in_file_out_file(in_file=None, out_file=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global result
            try:
                file_open = open(in_file, "r", encoding="utf-8")
                file_log = open(out_file, "w", encoding="utf-8")
            except FileNotFoundError:
                print("Файл не найден")
            else:
                args = (file_open, file_log, *args)
                result = func(*args, **kwargs)
                file_open.close()
                file_log.close()
            return result

        return wrapper

    return decorator


file_read = 'homework.txt'
file_write = 'test_out.txt'


@in_file_out_file(file_read, file_write)
def analysis_and_summarize_file(in_file, out_file):
    out_str = f"В файле: {in_file.name}" + "\n"
    text_analysis = [[word.strip(",.!? _") for word in line.strip().split() if word.isalpha()] for line in in_file]
    vowels_str = "aeuioyаеяоиё"
    count_lines = len(text_analysis)
    count_words = 0
    count_vowels = 0
    count_consonants = 0
    average_world_length = []
    short_word = text_analysis[0][0]
    longest_word = text_analysis[0][0]
    for line in text_analysis:
        count_words += len(line)
        for word in line:
            average_world_length.append(len(word))
            if len(word.lower()) > len(longest_word.lower()):
                longest_word = word
            elif len(word.lower()) < len(short_word.lower()):
                short_word = word
            for symbol in word:
                if symbol in vowels_str:
                    count_vowels += 1
                else:
                    count_consonants += 1
    out_str = out_str + f"Количество строк: {count_lines}" + "\n" \
                        f"Количество слов: {count_words}" + "\n" \
                        f"Количество гласных букв: {count_vowels}" + "\n" \
                        f"Количество согласных букв: {count_consonants}" + "\n" \
                        f"Средняя длинна слова: {int(sum(average_world_length) / count_words)}" + "\n" \
                        f"Самое короткое слово: {short_word}" + "\n" \
                        f"Самое длинное слово: {longest_word}" + "\n"
    out_file.write(out_str)
    print(f"Отчет записан в файл: {out_file.name}")


def encryption_logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(f'date: {timestamp}; {func.__name__}-filename: {result[0]}; key: {result[1]};')
        return result

    return wrapper


@encryption_logging
def write_key():
    file_name = "crypto.key"
    if os.path.isfile(file_name):
        with open(file_name, "rb") as f:
            return file_name, f.read()
    else:
        key = Fernet.generate_key()
        with open(file_name, "wb") as key_file:
            key_file.write(key)
            return file_name, key


@encryption_logging
def load_key():
    file_name = "crypto.key"
    with open(file_name, "rb") as key_load:
        return file_name, key_load.read()


@encryption_logging
def remove_file_key(file_name):
    try:
        os.remove(file_name)
        return file_name, "File deleted"
    except FileNotFoundError:
        return file_name, "File does not exist"


@encryption_logging
def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, 'rb') as f:
        data = f.read()

    encrypted_text = cipher.encrypt(data)
    encrypted_filename = "encrypted" + os.path.splitext(filename)[1]
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_text)

    return encrypted_filename, key


@encryption_logging
def decrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, 'rb') as fr:
        encrypted_data = fr.read()
    decrypted_data = cipher.decrypt(encrypted_data).decode(encoding="utf-8")
    decrypted_filename = "decrypted" + os.path.splitext(filename)[1]
    with open(decrypted_filename, 'w', encoding="utf-8", newline='') as f:
        f.write(decrypted_data)

    return decrypted_filename, key


total_size = 0


def analysis_file_sizes(path):
    global total_size
    for i in os.listdir(path):
        if os.path.isdir(fr"{path}\{i}"):
            analysis_file_sizes(fr"{path}\{i}")
        elif os.path.isfile(fr"{path}\{i}"):
            total_size += os.path.getsize(fr"{path}\{i}")
    if total_size < 1024:
        return f"{total_size} байт"
    elif total_size < 1024 ** 2:
        return f"{round(total_size / 1024, 2)} КБ"
    elif total_size < 1024 ** 3:
        return f"{round(total_size / 1024 ** 2, 2)} МБ"
    else:
        return f"{round(total_size / 1024 ** 3, 2)} ГБ"



def main():
    while (user_answer := input("Make your choice:\n"
                                "1. analysis and summarize file\n"
                                "2. encrypt_file and decrypt_file\n"
                                "3. analysis file sizes\n"
                                "'q' quit\n: ")) != "q":
        match user_answer:
            case "1":
                analysis_and_summarize_file()
            case "2":
                while (query := input("Make your choice:\n"
                                      "1. Create secret key\n"
                                      "2. Input file name encrypted\n"
                                      "3. Input file name decrypted\n"
                                      "4. Remove secret key\n"
                                      "'0' Exit\n: ")) != "0":
                    match query:
                        case "1":
                            write_key()
                        case "2":
                            key = load_key()[1]
                            file_name = input("Enter a filename to encrypt\n: ")
                            encrypt_file(file_name, key)
                        case "3":
                            key = load_key()[1]
                            file_name = input("Enter filename to decrypt\n: ")
                            decrypt_file(file_name, key)
                        case"4":
                            if input("Warning when deleting directory, private key will be permanently deleted\n"
                                     "1. Confirm\n: ") == "1":
                                remove_file_key("crypto.key")
                            else:
                                print("The secret key has not been deleted!")
                        case _:
                            print("There is not command like this.")
            case "3":
                dir_path_input = input("Enter directory path\n: ")
                print(analysis_file_sizes(dir_path_input))
            case _:
                print("There is no command like this.")
    else:
        print("See you soon!!")


if __name__ == '__main__':
    main()

