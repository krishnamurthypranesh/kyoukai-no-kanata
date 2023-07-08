from typing import List, Optional

from fastapi import APIRouter, Depends


OpsRouter = APIRouter(prefix="/v1/ops")

@OpsRouter.get("")
def get_ops():
    return {"hello": "world"}


@OpsRouter.post("")
def do_op():
    return {"hello": "world"}

