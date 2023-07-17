"""
Main file for the linkedlist service.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import linkedlist_enpoint_helpers as linked_list_help
from common import config_info

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """Redirect to /docs.
    """
    return RedirectResponse("/docs")


@app.get("/get-all-linked-lists")
async def get_all_linked_lists():
    """Function that returns all the existing lists.

        Args:

        Returns:
            a list containing all LinkedLists.
    """
    return linked_list_help.get_all_linked_lists()


@app.post("/create-linked-list/")
async def create_linked_list():
    """Endpoint that creates a new LinkedList and adds it into the 'database'.
    Args:

    Returns:
        the Id of the newly created LinkedList.
    """
    return linked_list_help.create_linked_list()


if __name__ == "__main__":
    uvicorn.run(
        app=config_info.LINKEDLIST_APP,
        host=config_info.HOST,
        port=config_info.LINKEDLIST_PORT,
        reload=True
    )
