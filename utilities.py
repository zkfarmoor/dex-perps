# utilities.py
import logging

def setup_logging(level):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def safe_execute(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
    return wrapper
