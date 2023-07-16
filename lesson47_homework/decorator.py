
from functools import wraps
from models.database import LOG_FILE_NAME


def save_results_to_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            with open(LOG_FILE_NAME, 'a', encoding='utf-8') as f:
                for row in result:
                    print(row, file=f)
            print(f"Results saved to file: {LOG_FILE_NAME}.")
            return result
        else:
            print("No data to save.")

    return wrapper
