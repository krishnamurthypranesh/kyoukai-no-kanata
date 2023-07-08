
import sqlalchemy

from app  import config

def db_session_factory():
    db_conf = config.get_db_config()

    url = f"postgresql+psycopg2://{db_conf.user}:{db_conf.passwd}@{db_conf.host}:{db_conf.port}/{db_conf.name}"

    engine = sqlalchemy.create_engine(
        url,
        echo=config.ROOTCONFIG["database"]["echo"],
        pool_size=config.ROOTCONFIG["database"]["pool"]["size"],
        pool_recycle=config.ROOTCONFIG["database"]["pool"]["recycle"],
        pool_timeout=config.ROOTCONFIG["database"]["pool"]["timeout"],
    )

    _sessionmaker = sqlalchemy.orm.sessionmaker(
        bind=engine,
        autocommit=config.ROOTCONFIG["database"]["session"]["auto_commit"],
        autoflush=config.ROOTCONFIG["database"]["session"]["auto_flush"],
        expire_on_commit=config.ROOTCONFIG["database"]["session"]["expire_on_commit"],
    )

    return engine, _sessionmaker

