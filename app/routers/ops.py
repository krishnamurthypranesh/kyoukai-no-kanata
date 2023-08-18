import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.clients import HttpbinClient
from app.config import get_app_config
from app.database import get_db
from app.models import RequestReceived
from app.schema import DoOpRequest, ListOpsRequest, ListOpsResponse, DoOpServiceParams
from app.services import OpsService


OpsRouter = APIRouter(prefix="/v1/ops")

logger = logging.getLogger(__name__)

@OpsRouter.get("")
def get_ops(
    db: Session = Depends(get_db),
):
    app_config = get_app_config()
    httpbin_client = HttpbinClient(app_config.httpbin_url)

    svc = OpsService(db=db, client=httpbin_client)
    out = svc.list_ops(params=DoOpServiceParams())

    return ListOpsResponse(
        count=out.count,
        records=out.records,
        next=out.next,
        prev=out.prev,
    )


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

