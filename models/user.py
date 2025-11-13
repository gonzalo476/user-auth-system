from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    email: Optional[str] = None
    department: Optional[str] = None
    password: Optional[str] = None
