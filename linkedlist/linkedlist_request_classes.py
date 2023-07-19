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
