from sqlalchemy.orm import Session

from app.clients import HttpbinClient
from app.schema import DoOpServiceParams, DoOpServiceResponse, ListOpsServiceParams, ListOpsServiceResponse
from app.services.base import BaseService

class OpsService(BaseService):
    def __init__(self, db: Session, httpbin_client: HttpbinClient):
        self.db = db
        self.httpbin_client = httpbin_client

    def do_op(self, params: DoOpServiceParams) -> DoOpServiceResponse:
        # call httpbin
        # save the entry in the database
        # return the uuid
        pass

    def list_ops(self, params: ListOpsServiceParams) -> ListOpsServiceResponse:
        # query the database to list the records
        # return the list
        pass


