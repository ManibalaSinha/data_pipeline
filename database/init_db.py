import sys
import os
import asyncio
from models.base import Base  # your declarative base
from models.note import Note
from database.session import engine

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized!")

asyncio.run(init_db())