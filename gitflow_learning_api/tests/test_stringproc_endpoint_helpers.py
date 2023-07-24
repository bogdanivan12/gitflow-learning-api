"""
Testing module
"""
import json
from starlette.responses import JSONResponse

from gitflow_learning_api.stringproc.\
    stringproc_endpoint_helpers import char_rmv, get_char_occ
from gitflow_learning_api.stringproc.\
    stringproc_request_classes import CustomString


def test_happy_get_char_occ1() -> None:
    """
    Test for get_char_occ when the given input is correct
    """
    param = "asdasd"
    expct_r = {"a": 2, "s": 2, "d": 2}
    actual_r = get_char_occ(param)
    assert expct_r == json.loads(actual_r.body.decode())


##############################################


def test_not_happy_get_char_occ_1() -> None:
    """
    Test for get_char_occ when the string provided is not correct
    """
    param = "asdasd*"
    expct_r = JSONResponse\
        (status_code=200,content={"Error":"Word must contain only ascii"})
    actual_r = get_char_occ(param)
    assert json.loads(expct_r.body.decode()) \
           == json.loads(actual_r.body.decode())


def test_happy_char_rmv_1() -> None:
    """
    Test for char_rmv when the given input is correct (letters and int)
    """
    param = CustomString(string="asd12f3", calculate_sum=True)
    expct_r = JSONResponse(status_code=200,
                           content={"stripped_strings": "123",
                                    "numeric_sum": 6
                                    })
    actual_r = char_rmv(param)
    assert json.loads(expct_r.body.decode()) \
           == json.loads(actual_r.body.decode())


def test_not_happy_char_rmv_1() -> None:
    """
    Test when the given input is
    not correct (contains not letter-int characters)
    """
    param = CustomString(string="%asd^12f3*", calculate_sum=True)
    expct_r = JSONResponse(
        status_code=200,
        content={
            "Error":
                "Word must be up to 255 "
                "characters and must be alphanumeric"
        })
    actual_r = char_rmv(param)
    assert json.loads(expct_r.body.decode())\
           == json.loads(actual_r.body.decode())
