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


def show_linked_list(name: str):
    """
    Endpoint that is responsible for showing the nodes of the requested linked
    list.

    Args:
        name (str): the name of the LinkedList to be shown.

    Returns:
        list (array): array containing the values of the nodes in the requested
        LinkedList.
    """
    response = {
        "list": [],
        "message": "LinkedList not found."
    }

    if name not in linked_lists_dict:
        return response

    linked_list = linked_lists_dict[name]

    try:
        aux = linked_list.head
        while aux is not None:
            response["list"].append(str(aux.value))
            aux = aux.next_node
        response["message"] = "Success."
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


def length(name: str):
    """
    Endpoint that is responsible for showing the length of the requested linked
    list.

    Args:
        name (str): the name of the requested LinkedList.

    Returns:
        length (int): the length of the LinkedList
        message (str): the state of the operation.
    """
    response = {
        "length": None,
        "message": "LinkedList not found."
    }

    if name not in linked_lists_dict:
        return response

    linked_list = linked_lists_dict[name]

    try:
        response = {
            "length": len(linked_list),
            "message": "Success."
        }
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


def push_back(item: linkedlist_req.PushBackRequest):
    """
    Endpoint that is responsible for the push_back operation.

    Args:
         item:
            name (str): the name of the LinkedList.
            value (str): the value to be pushed in the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    item_dict = item.dict()
    response = {"message": "LinkedList not found."}

    if item_dict["name"] not in linked_lists_dict:
        return response

    linked_list = linked_lists_dict[item_dict["name"]]
    value = item_dict["value"]

    try:
        if linked_list.head is None:
            linked_list.head = linkedlist_classes.Node(value)
        else:
            aux = linked_list.head
            while aux.next_node is not None:
                aux = aux.next_node
            aux.next_node = linkedlist_classes.Node(value)
        response["message"] = "Success."
        pickle_dump_linked_lists()
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


def push_front(item: linkedlist_req.PushFrontRequest):
    """
    Endpoint that is responsible for the push_front operation.

    Args:
         item:
            name (str): the name of the LinkedList.
            value (str): the value to be pushed into the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    item_dict = item.dict()
    response = {"message": "LinkedList not found."}

    if item_dict["name"] not in linked_lists_dict:
        return response

    linked_list = linked_lists_dict[item_dict["name"]]
    value = item_dict["value"]

    try:
        if linked_list.head is None:
            linked_list.head = linkedlist_classes.Node(value)
        else:
            linked_list.head = linkedlist_classes.Node(value, linked_list.head)
        response["message"] = "Success."
        pickle_dump_linked_lists()
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


def insert(item: linkedlist_req.InsertRequest):
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
    item_dict = item.dict()
    response = {"message": "LinkedList not found."}

    if item_dict["name"] not in linked_lists_dict:
        return response

    linked_list = linked_lists_dict[item_dict["name"]]
    value = item_dict["value"]
    position = item_dict["position"]

    if len(linked_list) < position:
        response["message"] = "The LinkedList is too short."
        return response

    if position == 0:
        return push_front(
            linkedlist_req.PushFrontRequest(
                name=item_dict["name"],
                value=value
            )
        )

    if position == len(linked_list):
        return push_back(
            linkedlist_req.PushBackRequest(
                name=item_dict["name"],
                value=value
            )
        )

    try:
        aux = linked_list.head
        i = 0
        while i < position - 1:
            aux = aux.next_node
            i += 1
        new_node = linkedlist_classes.Node(value, aux.next_node)
        aux.next_node = new_node

        response["message"] = "Success."
        pickle_dump_linked_lists()
    except Exception as error:
        response["message"] = f"Encountered error: {error}"

    return response


def clear_linked_list(item: linkedlist_req.ClearLinkedListRequest):
    """
    Endpoint that is responsible for deleting all nodes in a linked list.

    Args:
         item:
            name (str): the name of the LinkedList.

    Returns:
        message (str): the state of the operation.
    """
    item_dict = item.dict()
    linked_list = linked_lists_dict[item_dict["name"]]

    response = {
        "message": "Success."
    }

    try:
        while linked_list.head is not None:
            aux = linked_list.head
            linked_list.head = linked_list.head.next_node
            del aux
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
