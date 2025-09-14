from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from api.dependencies import get_current_user, get_db_session as get_db

from models.note import Note
from schemas.note import NoteCreate, NoteUpdate, NoteOut
from database.session import AsyncSessionLocal
from api.dependencies import get_current_user, get_db  # JWT & DB dependency

router = APIRouter(prefix="/notes", tags=["notes"])

# Create Note
@router.post("/", response_model=NoteOut)
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    new_note = Note(**note.dict(), owner_id=current_user.id)
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

# Read All Notes (current user)
@router.get("/", response_model=List[NoteOut])
async def read_notes(db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    result = await db.execute(
        "SELECT * FROM notes WHERE owner_id = :owner_id", {"owner_id": current_user.id}
    )
    notes = result.fetchall()
    return [NoteOut.from_orm(n) for n in notes]

# Read Single Note
@router.get("/{note_id}", response_model=NoteOut)
async def read_note(note_id: int, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    note = await db.get(Note, note_id)
    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

# Update Note
@router.put("/{note_id}", response_model=NoteOut)
async def update_note(note_id: int, note_update: NoteUpdate, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    note = await db.get(Note, note_id)
    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    for key, value in note_update.dict(exclude_unset=True).items():
        setattr(note, key, value)

    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note

# Delete Note
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    note = await db.get(Note, note_id)
    if not note or note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    await db.delete(note)
    await db.commit()
    return None
