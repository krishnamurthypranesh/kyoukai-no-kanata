from sqlalchemy.orm import Session

from app.models import RequestReceived
from app.repo.base import RepoBase


class RequestReceivedRepo(RepoBase):
    def get_all(self, db: Session):
        return db.query(RequestReceived).all()