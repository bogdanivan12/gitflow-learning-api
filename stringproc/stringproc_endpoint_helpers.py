"""
Module with helper functions for end points
"""
import string
import logging
from functools import wraps
from typing import Callable
from collections import Counter

from fastapi.responses import JSONResponse

from stringproc_request_classes import CustomString



logging.basicConfig(filename="log.txt", filemode="w",
                    format="[%(asctime)s] [PID:%(process)d ] [%(module)s: %(lineno)d] "
                           " [%(levelname)s] %(message)s",
                    level=logging.DEBUG)


def validator_custom(fnc: Callable):

    @wraps(fnc)
    def inner(*args, **kwargs) -> JSONResponse:
        logging.warning("pizza")
        try:
            logging.info("Function %s called",fnc.__name__)
            return JSONResponse(status_code=200, content=fnc(*args, **kwargs))
        except ValueError as error_e:
            logging.warning("Error when called function %s  -   %s",fnc.__name__, error_e)
            return JSONResponse(status_code=200, content={"Error": f"{error_e}"})

    return inner


@validator_custom
def get_char_occ(word: str):
    if not set(word) <= set(string.ascii_letters):
        raise ValueError("Word must contain only ascii letters")
    return Counter(word)


@validator_custom
def char_rmv(word: CustomString):
    if len(word.string) > 255 or len(word.string) < 1 \
            or (not set(word.string) <= set(string.ascii_letters + string.digits)):
        raise ValueError("Word must be up to 255 characters and must be alphanumeric")

    statement = "".join(filter(lambda x: not x.isalpha() , word.string))

    sum1 = None
    if word.calculate_sum:
        sum1 = sum(int(x) for x in statement)

    return {"stripped_strings": "".join(statement),
            "numeric_sum": sum1
            }
