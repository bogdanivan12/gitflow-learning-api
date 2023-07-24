"""
Main module to start api
"""


#sys.path.append(str(pathlib.Path(os.path.join
# (os.getcwd(), "../..")).resolve()))

import fastapi

import uvicorn
from starlette.responses import JSONResponse

import stringproc_endpoint_helpers

from stringproc_request_classes import CustomString
from gitflow_learning_api.common import config_info

app = fastapi.FastAPI()


@app.get("/", response_class=fastapi.responses.RedirectResponse
    , include_in_schema=False)
def redir():
    """
    Functie de redirectare catre documentatie pe ruta de baza
    """
    return fastapi.responses.RedirectResponse(url="/docs")


@app.get("/get-char-occurrences/{word}")
def char_occ(word: str) -> JSONResponse:
    """
    Functie ce intoarce un
     JSONResponse cu numarul de aparitii a unui caracter
    :param word: string
    :return: JSONResponse
    """
    return stringproc_endpoint_helpers.get_char_occ(word)


@app.post("/remove-letters-from-string")
def rmv_letters(word: CustomString) -> JSONResponse:
    """
    Functie ce intoarce un JSONResponse care intoarce stringul
    din payload fara litere si (in functie de
    valoarea unui alt parametru  intoarce fie None fie suma
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
