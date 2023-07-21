"""File containing request classes definitions for endpoints request bodies."""
from pydantic import BaseModel


class CreateLinkedListRequest(BaseModel):
    """
    Class that represents the request body for the create-linked-list endpoint.
    """
    name: str


class DeleteLinkedListRequest(BaseModel):
    """
    Class that represents the request body for the delete-linked-list endpoint.
    """
    name: str


class PushBackRequest(BaseModel):
    """
    Class that represents the request body for the push-back endpoint.
    """
    name: str
    value: str


class PushFrontRequest(BaseModel):
    """
    Class that represents the request body for the push-front endpoint.
    """
    name: str
    value: str


class InsertRequest(BaseModel):
    """
    Class that represents the request body for the insert endpoint.
    """
    name: str
    value: str
    position: int
