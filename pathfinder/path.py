from typing import TypedDict
from pathfinder.city import City

class Path(TypedDict):
    total: float
    steps: list[City]