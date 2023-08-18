import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from app import config 

@pytest.fixture(scope="session")
def provide_engine():
    db_conf = config.get_db_config()

    url = f"postgresql+psycopg2://{db_conf.user}:{db_conf.passwd}@localhost:{db_conf.port}/{db_conf.name}"

    eng = sqlalchemy.create_engine(
        url,
        echo=config.ROOTCONFIG["database"]["echo"],
        pool_size=config.ROOTCONFIG["database"]["pool"]["size"],
        pool_recycle=config.ROOTCONFIG["database"]["pool"]["recycle"],
        pool_timeout=config.ROOTCONFIG["database"]["pool"]["timeout"],
    )

    eng = eng.execution_options(isolation_level="READ_COMMITED")

    return eng


@pytest.fixture(scope="function")
def provide_db(provide_engine):
    eng = provide_engine

    db = sessionmaker(bind=eng)
    db.expire_on_commit = False
    
    try:
        yield db
    finally:
        db.close()
