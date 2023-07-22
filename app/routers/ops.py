import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import RequestReceived
from app.schema import DoOpRequest, ListOpsRequest
from app.services import OpsService


OpsRouter = APIRouter(prefix="/v1/ops")

logger = logging.getLogger(__name__)

@OpsRouter.get("")
def get_ops(
    db: Session = Depends(get_db),
):
    records = db.query(RequestReceived).all()
    logger.info(records)

    response = []

    for r in records:
        response.append({
            "id": r.gid,
            "request": r.request,
            "response": r.response,
            "created_at": r.created_at,
            "updated_at": r.updated_at,
        })

    return response


@OpsRouter.post("")
def do_op(
    request: DoOpRequest,
    db: Session = Depends(get_db),
):
    # make request to generate uuid
    # save the entry in the database
    # return the uuid
    return {"hello": "world"}

