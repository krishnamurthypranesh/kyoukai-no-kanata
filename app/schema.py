from typing import List

from pydantic import BaseModel

from app.models import RequestReceived

class CustomBase(BaseModel):
    pass


class DoOpRequest(CustomBase):
    key: str
    value: str


class DoOpResponse(CustomBase):
    pass


class ListOpsRequest(CustomBase):
    pass


class ListOpsResponse(CustomBase):
    pass


class DoOpServiceParams(CustomBase):
    pass


class DoOpServiceResponse(CustomBase):
    uuid: str


class ListOpsServiceParams(CustomBase):
    pass


class ListOpsServiceResponse(CustomBase):
    count: int
    records: List[RequestReceived]
    next: str
    prev: str

    class Config:
        arbitrary_types_allowed = True
