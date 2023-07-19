"""
Main file for the linkedlist service.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import linkedlist_endpoint_helpers as linkedlist_help
import linkedlist_request_classes as linkedlist_req
from common import config_info

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """
    Redirect to /docs.
    """
    return RedirectResponse("/docs")


@app.get("/get-all-linked-lists")
async def get_all_linked_lists():
    """
    Function that returns all the existing lists.

    Args:

    Returns:
        a list containing all LinkedLists.
    """
    return linkedlist_help.get_all_linked_lists()


@app.post("/create-linked-list/")
async def create_linked_list(item: linkedlist_req.CreateLinkedListRequest):
    """
    Endpoint that creates a new LinkedList and adds it into the 'database'.

    Args:
        item:
            name (str): the name of the new list to be created.
    Returns:

    """
    return linkedlist_help.create_linked_list(item)


@app.post("/delete-linked-list/")
async def delete_linked_list(item: linkedlist_req.DeleteLinkedListRequest):
    """
    Endpoint that deletes a LinkedList found by its name.

    Args:
         item:
            name (str): the name of the LinkedList to be deleted.

    Returns:

    """
    return linkedlist_help.delete_linked_list(item)


if __name__ == "__main__":
    uvicorn.run(
        app=config_info.LINKEDLIST_APP,
        host=config_info.HOST,
        port=config_info.LINKEDLIST_PORT,
        reload=True
    )
