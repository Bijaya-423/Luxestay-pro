from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.folio import Folio
from app.models.folio_item import FolioItem

def get_folios(db: Session):
    return db.query(Folio).all()

def create_folio(data, db: Session):
    folio = Folio(
        booking_id= data.booking_id,
        room_id = data.room_id
    )
    db.add(folio)
    db.commit()
    db.refresh(folio)

    total = 0
    
    for item in data.items:
        obj = FolioItem(
            folio_id = folio.id,
            item_type = item.item_type,
            description = item.description,
            amount = item.amount
        )
        total += item.amount
        db.add(obj)
    
    folio.total_amount = total
    db.commit()

    return folio

def get_folio(id: int, db: Session):
    obj = db.query(Folio).filter(Folio.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Folio Not Found.")

    return obj

def update_folio(id: int, data, db: Session):
    obj = db.query(Folio).filter(Folio.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Folio not found.")
    
    obj.status = data.status
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj

def update_folio(id: int, db: Session):
    obj = db.query(Folio).filter(Folio.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Found Not Found.")

    return obj


def delete_folio(id: int, db: Session):
    folio = db.query(Folio).filter(Folio.id == id).first()

    if not folio:
        raise HTTPException(status_code=404, detail="Folio not Found.")

    db.delete(folio)
    db.commit()

    return {"message": "Deleted Successfully"}


def get_folio_details(id: int, db: Session):

    folio = db.query(Folio).filter(Folio.id == id).first()

    if not folio:
        raise HTTPException(status_code=404, detail="Folio Not Found.")

    items = db.query(FolioItem).filter(FolioItem.folio_id == id).all()

    return {
        'folio' : folio,
        "items": items
    }


# def get_folio_by_booking(booking_id: int, db: Session):
#     folio = db.query(Folio).filter(Folio.booking_id == booking_id).first()

#     if not folio:
#         raise HTTPException(status_code=404, detail="Folio Not Found.")

#     items = db.query(FolioItem).filter(FolioItem.folio_id == folio.id).all()

#     return {
#         'folio' : folio,
#         "items": items
#     }
