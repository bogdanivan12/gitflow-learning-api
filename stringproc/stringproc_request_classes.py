
from pydantic import BaseModel



def snake_to_camel(val: str)->str:

    word = "".join([f"{i[0].capitalize()}{i[1:]}" for i in val.strip().split("_")])
    return f"{word[0].lower()}{word[1:]}"


class CustomString(BaseModel):

    string: str
    calculate_sum: bool

    class Config:

        populate_by_name = True
        extra = 'allow'
        alias_generator = snake_to_camel
