import os
import logging
from logging.config import fileConfig

from alembic import context
import envyaml

from app.connectors import db_session_factory
from app import config
from app import models

alembic_config = context.config

fileConfig(alembic_config.config_file_name)

target_metadata = models.Base.metadata


def run_migration_offline():
    db_conf = config.get_db_config()

    conn_url = f"postgresql://{db_conf.user}:{db_conf.passwd}@{db_conf.host}:{db_conf.port}/{db_conf.database}"

    context.configure(
        url=conn_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_types=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    config_file = os.environ.get("APP_CONFIG_YAML", "./config.yml")
    db_conf = envyaml.EnvYAML(config_file)["database"]
    db_conf["echo"] = True

    # figure this out
    engine, _ = db_session_factory()

    with engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_types=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migration_offline()
else:
    run_migrations_online()
