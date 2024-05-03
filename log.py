import logging
import time
from functools import wraps
import datetime


def log(level=logging.INFO):

    def current_datetime_ms():
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kzargs):
            czas_startu = time.time()
            wynik = func(*args, **kzargs)
            czas_zakonczenia = time.time()
            czas_wykonania = (czas_zakonczenia - czas_startu) * 1_000_000_000  # czas w nanosekundach
            argumenty = ', '.join([repr(arg) for arg in args])
            kzarg_znaczenia = ', '.join([f"{k}={v}" for k, v in kzargs.items()])
            all_args = ', '.join(filter(None, [argumenty, kzarg_znaczenia]))
            logger = logging.getLogger(__name__)
            logger.log(level, f"[{current_datetime_ms()}] Funkcja {func.__name__} wywołana z argumentami ({all_args}), {{}}.")
            logger.log(level, f"[{current_datetime_ms()}] Funkcja {func.__name__} zwraca {wynik}.")
            logger.log(level, f"[{current_datetime_ms()}] Funkcja {func.__name__} pracowała: {czas_wykonania:.6f} nanoseconds.")
            return wynik
        return wrapper
    return decorator
