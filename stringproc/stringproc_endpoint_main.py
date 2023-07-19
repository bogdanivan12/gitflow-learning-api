"""
Main module to start api
"""
from typing import Annotated

import fastapi

import uvicorn
from fastapi import Path
import common.config_info
import stringproc_endpoint_helpers

from starlette.responses import JSONResponse
from stringproc_request_classes import CustomString


app = fastapi.FastAPI()


@app.get("/", response_class=fastapi.responses.RedirectResponse, include_in_schema=False)
def redir():
    return fastapi.responses.RedirectResponse(url="/docs")


@app.get("/get-char-occurrences/{word}")
def char_occ(word: Annotated[str, Path(title="word to get occurrences")]) -> JSONResponse:
    return stringproc_endpoint_helpers.get_char_occ(word)


@app.post("/remove-letters-from-string")
def rmv_letters(word: CustomString) -> JSONResponse:
    return stringproc_endpoint_helpers.char_rmv(word)


if __name__ == '__main__':
    uvicorn.run("stringproc_main:app",
                host=common.config_info.STRINGPROC_APP,
                port=common.config_info.STRINGPROC_PORT,
                reload=True
                )
