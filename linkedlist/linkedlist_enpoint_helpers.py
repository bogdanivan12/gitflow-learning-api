"""
File containing the endpoint helpers definitions for the linkedlist services.
"""
import pickle

import linkedlist_classes
import linkedlist_request_classes as linkedlist_req

linked_lists_dict = {}


def pickle_dump_linked_lists():
    """
    Function that saves current linked lists into a file.
    """
    with open("db_linked_lists", "wb") as file:
        pickle.dump(linked_lists_dict, file)


def get_all_linked_lists():
    """
    Function that returns all the existing lists.

    Args:

    Returns:
        a list containing all LinkedLists names.
    """
    global linked_lists_dict
    response = {
        "lists": list(linked_lists_dict.keys()),
        "message": "Success."
    }
    return response


def create_linked_list(item: linkedlist_req.CreateLinkedListRequest):
    """
    Endpoint that creates a new LinkedList and adds it into the 'database'.

    Args:
        item:
            name (str): the name of the new list to be created.
    Returns:

    """
    global linked_lists_dict
    response = {"message": "Success."}

    name = item.dict()["name"]
    if name in linked_lists_dict:
        response["message"] = f"A LinkedList named '{name}' already exists."
        return response

    try:
        new_linked_list = linkedlist_classes.LinkedList(name)
        linked_lists_dict[name] = new_linked_list
        pickle_dump_linked_lists()
    except Exception as error:
        response["message"] = f"Encountered error: {error}."

    return response


def delete_linked_list(item: linkedlist_req.DeleteLinkedListRequest):
    """
    Endpoint that deletes a LinkedList found by its name.

    Args:
         item:
            name (str): the name of the LinkedList to be deleted.

    Returns:

    """
    global linked_lists_dict
    item_dict = item.dict()
    response = {"message": "LinkedList not found."}

    if item_dict["name"] not in linked_lists_dict:
        return response

    try:
        linked_lists_dict.pop(item_dict["name"])
        response["message"] = "Success."
        pickle_dump_linked_lists()
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


# Load linked_list_dict when the service starts.
try:
    with open("db_linked_lists", "rb") as file:
        linked_lists_dict = pickle.load(file)
except FileNotFoundError:
    linked_lists_dict = {}
    pickle_dump_linked_lists()
