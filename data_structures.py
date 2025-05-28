
# This module defines various data structures in Python.
from typing import List, Tuple, Set, Dict, Union, TypedDict

# tuples
tuple_example: Tuple[int, str, float] = (1, "example", 3.14)

# lists
list_example: List[int] = [1, 2, 3, 4, 5]

# sets
set_example: Set[str] = {"apple", "banana", "cherry"}

# union types
union_example: int | str = 42  # can be either an int or a str

# union types alt
alt_union_example: Union[int, str] = 42  # can be either an int or a str

# dictionaries
dict_example: Dict[str, int] = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# heterogeneous dictionary
object_example: dict[str, str | int] = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# -- or --
alt_object_example: dict[str, Union[str, int]] = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# typed dictionary
class Person(TypedDict):
    name: str
    age: int
    city: str

# typed dictionary example
person_example: Person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# typed dictionary with optional fields
class PersonWithOptional(TypedDict, total=False):
    name: str
    age: int
    city: str
    country: str  # optional field

# typed dictionary example with optional fields
person_optional_example: PersonWithOptional = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    # 'country' is optional and can be omitted
}
