from typing import Any

from sqlalchemy.orm import Session

class RepoBase:
    def insert(self, db: Session, record: Any):
        db.add(instance=record)
        db.flush()