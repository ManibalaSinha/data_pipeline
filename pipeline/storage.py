from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from pipeline.config import load_settings

settings = load_settings()
DB_URL = settings['storage']['db_url']

engine: Engine = create_engine(DB_URL, pool_size=10, max_overflow=20)
metadata = MetaData()

posts = Table(
    'posts', metadata,
    Column('post_id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('title', String(255)),
    Column('body', Text),
)

def init_db():
    metadata.create_all(engine)

@contextmanager
def get_conn():
    conn = engine.connect()
    trans = conn.begin()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()

def upsert_posts(conn, post_dicts):
    stmt = insert(posts).values(post_dicts)
    stmt = stmt.on_conflict_do_update(
        index_elements=['post_id'],
        set_={
            'title': stmt.excluded.title,
            'body': stmt.excluded.body,
            'user_id': stmt.excluded.user_id,
        }
    )
    try:
        conn.execute(stmt)
    except SQLAlchemyError as e:
        raise

if __name__ == '__main__':
    init_db()
    print('DB initialized')
