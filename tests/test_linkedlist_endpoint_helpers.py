"""File containing unit testing functions."""
from linkedlist import linkedlist_endpoint_helpers as linkedlist_help
from linkedlist import linkedlist_request_classes as linkedlist_req
from linkedlist import linkedlist_classes


def test_get_all_linked_lists_empty():
    linkedlist_help.linked_lists_dict = {}
    expected_response = {
        "lists": [],
        "message": "Success."
    }
    actual_response = linkedlist_help.get_all_linked_lists()
    assert expected_response == actual_response


def test_get_all_linked_lists_not_empty():
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


def test_create_linked_list_already_exists():
    linkedlist_help.linked_lists_dict = {}
    request = linkedlist_req.CreateLinkedListRequest(name="xyz")
    response = linkedlist_help.create_linked_list(request)
    response = linkedlist_help.create_linked_list(request)
    assert response["message"] != "Success."


def test_happy_delete_linked_list():
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


def test_delete_linked_list_not_found():
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
