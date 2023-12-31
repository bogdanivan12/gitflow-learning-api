"""
Module for pydantic classes
"""
from pydantic import BaseModel



def snake_to_camel(val: str)->str:
    """
    :param val: Value in snake case to be converted in camel_case
    :return: camel case of the string provided
    """
    word = "".join([f"{i[0].capitalize()}"
                    f"{i[1:]}" for i in val.strip().split("_")])
    return f"{word[0].lower()}{word[1:]}"


class CustomString(BaseModel):
    """
    Custom class with pydantic as a base for fastapi
    """
    string: str
    calculate_sum: bool

    class Config:
        """
        Config class
        -> populate by name :
           allows using either field aliases or field names
        ->extra: allows extra parameters
        -> alias generator:
            allows alias generated by a given function
        """
        populate_by_name = True
        extra = 'allow'
        alias_generator = snake_to_camel
