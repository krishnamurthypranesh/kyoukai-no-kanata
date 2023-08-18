import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.clients import HttpbinClient
from app.config import get_app_config
from app.database import get_db
from app.models import RequestReceived
from app.schema import DoOpRequest, ListOpsRequest, DoOpServiceParams
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
    app_config = get_app_config()
    httpbin_client = HttpbinClient(app_config.httpbin_url)

    svc = OpsService(db=db, client=httpbin_client)
    out = svc.do_op(params=DoOpServiceParams())

    return {"uuid": out.uuid}

