"""File containing unit testing functions."""
from gitflow_learning_api.linkedlist \
    import linkedlist_classes
from gitflow_learning_api.linkedlist \
    import linkedlist_request_classes as linkedlist_req
from gitflow_learning_api.linkedlist \
    import linkedlist_endpoint_helpers as linkedlist_help


def test_get_all_linked_lists_empty():
    """Test for get_all_linked_list endpoint when no list was created."""
    linkedlist_help.linked_lists_dict = {}
    expected_response = {
        "lists": [],
        "message": "Success."
    }
    actual_response = linkedlist_help.get_all_linked_lists()
    assert expected_response == actual_response


def test_get_all_lists_not_empty():
    """Test for get_all_linked_list endpoint when some lists were created."""
    linkedlist_help.linked_lists_dict = {
        "test": linkedlist_classes.LinkedList("test"),
        "abc": linkedlist_classes.LinkedList("abc")
    }
    expected_response = {
        "lists": ["test", "abc"],
        "message": "Success."
    }
    actual_response = linkedlist_help.get_all_linked_lists()
    assert expected_response == actual_response


def test_happy_create_linked_list():
    """
        Test for create_linked_list endpoint when the list is
        successfully created.
    """
    linkedlist_help.linked_lists_dict = {}
    request = linkedlist_req.CreateLinkedListRequest(name="xyz")
    response = linkedlist_help.create_linked_list(request)
    linked_lists = linkedlist_help.get_all_linked_lists()["lists"]
    assert response["message"] == "Success."
    assert linked_lists == ["xyz"]

    request = linkedlist_req.CreateLinkedListRequest(name="abc")
    response = linkedlist_help.create_linked_list(request)
    linked_lists = linkedlist_help.get_all_linked_lists()["lists"]
    assert response["message"] == "Success."
    assert linked_lists == ["xyz", "abc"]


def test_create_list_already_exists():
    """
        Test for create_linked_list endpoint when the list cannot be created
        because it already exists.
    """
    linkedlist_help.linked_lists_dict = {}
    request = linkedlist_req.CreateLinkedListRequest(name="xyz")
    response = linkedlist_help.create_linked_list(request)
    response = linkedlist_help.create_linked_list(request)
    assert response["message"] != "Success."


def test_happy_delete_linked_list():
    """
        Test for delete_linked_list endpoint when the list is
        successfully deleted.
    """
    linkedlist_help.linked_lists_dict = {
        "abc": linkedlist_classes.LinkedList("abc")
    }
    request = linkedlist_req.DeleteLinkedListRequest(name="abc")
    response = linkedlist_help.delete_linked_list(request)
    assert response["message"] == "Success."
    assert linkedlist_help.linked_lists_dict == {}

    linkedlist_help.linked_lists_dict = {
        "abc": linkedlist_classes.LinkedList("abc"),
        "xyz": linkedlist_classes.LinkedList("xyz")
    }
    response = linkedlist_help.delete_linked_list(request)
    assert response["message"] == "Success."
    assert linkedlist_help.get_all_linked_lists()["lists"] == ["xyz"]


def test_delete_list_not_found():
    """
        Test for delete_linked_list endpoint when the list cannot be deleted
        because it does not exists.
    """
    linkedlist_help.linked_lists_dict = {}
    request = linkedlist_req.DeleteLinkedListRequest(name="abc")
    actual_response = linkedlist_help.delete_linked_list(request)
    expected_response = {"message": "LinkedList not found."}
    assert actual_response == expected_response

    linkedlist_help.linked_lists_dict = {
        "xyz": linkedlist_classes.LinkedList("xyz")
    }
    actual_response = linkedlist_help.delete_linked_list(request)
    expected_response = {"message": "LinkedList not found."}
    assert actual_response == expected_response
