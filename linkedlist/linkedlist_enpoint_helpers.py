"""
File containing the endpoint helpers definitions for the linkedlist services.
"""
import linkedlist_classes

linkedLists = []


def get_all_linked_lists():
    """Function that returns all the existing lists.

        Args:

        Returns:
            a list containing all LinkedLists.
    """
    return {"lists": [list.id for list in linkedLists], "message": "Success."}


def create_linked_list():
    """Endpoint that creates a new LinkedList and adds it into the 'database'.
    Args:

    Returns:
        the Id of the newly created LinkedList.
    """
    response = {"id": None, "message": "Success."}

    try:
        newLinkedList = linkedlist_classes.LinkedList()
        linkedLists.append(newLinkedList)
        response["id"] = newLinkedList.id
    except Exception as e:
        response["message"] = f"Encountered error: {e}."

    return response
