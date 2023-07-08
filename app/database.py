from sqlalchemy.engine import Engine

engine = None
SessionLocal = None

def get_engine() -> Engine:
    return engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
