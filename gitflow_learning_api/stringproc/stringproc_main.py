"""
Main module to start api
"""
import fastapi

import uvicorn
from starlette.responses import JSONResponse

from gitflow_learning_api.common import config_info

from gitflow_learning_api.stringproc \
    import stringproc_request_classes
from gitflow_learning_api.stringproc \
    import stringproc_endpoint_helpers

app = fastapi.FastAPI()


@app.get("/", response_class=fastapi.responses.RedirectResponse
    , include_in_schema=False)
def redir():
    """
    Redirect function to docs route
    """
    return fastapi.responses.RedirectResponse(url="/docs")


@app.get("/get-char-occurrences/{word}")
def char_occ(word: str) -> JSONResponse:
    """
     Function which returns a
     JSONResponse with numbers of occurrences of a char in a str
    :param word: string
    :return: JSONResponse
    """
    return stringproc_endpoint_helpers.get_char_occ(word)


@app.post("/remove-letters-from-string")
def rmv_letters(word: stringproc_request_classes.CustomString) -> JSONResponse:
    """
    Function which returns a  JSONResponse which takes the
    string from payload without the letters and returns
    either the string without the numbers and none or the
    string without the numbers and the sum of those numbers
    :param word: CustomString (pydantic model)
    :return: JSONResponse
    """

    return stringproc_endpoint_helpers.char_rmv(word)


if __name__ == '__main__':
    uvicorn.run(
        app=config_info.STRINGPROC_APP,
        host=config_info.HOST,
        port=config_info.STRINGPROC_PORT,
        reload=True
    )
