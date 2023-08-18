from datetime import datetime

import ksuid
from sqlalchemy.orm import Session

from app.clients import HttpbinClient
from app.models import RequestReceived
from app.repo.requests_received import RequestReceivedRepo
from app.schema import DoOpServiceParams, DoOpServiceResponse, ListOpsServiceParams, ListOpsServiceResponse
from app.services.base import BaseService

class OpsService(BaseService):
    def __init__(self, db: Session, client: HttpbinClient):
        self.db = db
        self.client = client

    def do_op(self, params: DoOpServiceParams) -> DoOpServiceResponse:
        # call client
        uuid = self.client.generate_uuid()

        rec = RequestReceived(
            gid=str(ksuid.Ksuid()),
            request=params.json(),
            response={"uuid": uuid},
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        # save the entry in the database
        RequestReceivedRepo().insert(db=self.db, record=rec)

        self.db.commit()

        return DoOpServiceResponse(uuid=uuid)

    def list_ops(self, params: ListOpsServiceParams) -> ListOpsServiceResponse:
        # query the database to list the records
        # return the list
        pass


