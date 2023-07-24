"""
Main file for the linkedlist service.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import linkedlist_endpoint_helpers as linkedlist_help
import linkedlist_request_classes as linkedlist_req
from gitflow_learning_api.common import config_info

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


@app.get("/show-linked-list/{name}")
async def show_linked_list(name: str):
    """
    Endpoint that is responsible for showing the nodes of the requested linked
    list.

    Args:
        name (str): the name of the LinkedList to be shown.

    Returns:
        list (array): array containing the values of the nodes in the requested
        LinkedList.
        message (str): the state of the operation.
    """
    return linkedlist_help.show_linked_list(name)


@app.get("/length/{name}")
async def length(name: str):
    """
    Endpoint that is responsible for showing the length of the requested linked
    list.

    Args:
        name (str): the name of the requested LinkedList.

    Returns:
        length (int): the length of the LinkedList
        message (str): the state of the operation.
    """
    return linkedlist_help.length(name)


@app.post("/push-back/")
async def push_back(item: linkedlist_req.PushBackRequest):
    """
    Endpoint that is responsible for the push_back operation.

    Args:
         item:
            name (str): the name of the LinkedList.
            value (str): the value to be pushed into the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    return linkedlist_help.push_back(item)


@app.post("/push-front/")
async def push_front(item: linkedlist_req.PushFrontRequest):
    """
    Endpoint that is responsible for the push_front operation.

    Args:
         item:
            name (str): the name of the LinkedList.
            value (str): the value to be pushed into the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    return linkedlist_help.push_front(item)


@app.post("/insert/")
async def insert(item: linkedlist_req.InsertRequest):
    """
    Endpoint that is responsible for the push_front operation.

    Args:
         item:
            name (str): the name of the LinkedList.
            value (str): the value to be inserted into the LinkedList.
            position (int): the position of the newly inserted element in list.

    Returns:
        message (str): the state of the operation.
    """
    return linkedlist_help.insert(item)


@app.post("/clear-linked-list/")
async def clear_linked_list(item: linkedlist_req.ClearLinkedListRequest):
    """
    Endpoint that is responsible for deleting all nodes in a linked list.

    Args:
         item:
            name (str): the name of the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    return linkedlist_help.clear_linked_list(item)

if __name__ == "__main__":
    uvicorn.run(
        app=config_info.LINKEDLIST_APP,
        host=config_info.HOST,
        port=config_info.LINKEDLIST_PORT,
        reload=True
    )
