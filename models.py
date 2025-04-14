from pydantic import BaseModel
from typing import Optional, List, Any


class TrelloBoard(BaseModel):
    """Model representing a Trello board."""

    id: str
    name: str
    desc: Optional[str] = None
    closed: bool = False
    idOrganization: Optional[str] = None
    url: str


class TrelloList(BaseModel):
    """Model representing a Trello list."""

    id: str
    name: str
    closed: bool = False
    idBoard: str
    pos: float


class TrelloLabel(BaseModel):
    """Model representing a Trello label."""

    id: str
    idBoard: str
    name: Optional[str] = None
    color: Optional[str] = None
    uses: Optional[int] = None


class TrelloCard(BaseModel):
    """Model representing a Trello card."""

    id: str
    name: str
    desc: Optional[str] = None
    closed: bool = False
    idList: str
    idBoard: str
    url: str
    pos: float
    labels: Optional[List[TrelloLabel]] = None


class TrelloAttachment(BaseModel):
    """Model representing a Trello attachment."""
    id: str
    name: Optional[str] = None
    bytes: Optional[str] = None
    date: Optional[str] = None
    edgeColor: Optional[str] = None
    idMember: Optional[str] = None
    isUpload: bool = False
    mimeType: Optional[str] = None
    url: Optional[str] = None
    pos: Optional[float] = None
    previews: Optional[List[Any]] = None
