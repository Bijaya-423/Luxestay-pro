from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.folio_schema import FolioCreate, FolioUpdate
from app.controllers import folio_controller
from app.dependencies.auth_dependency import get_current_user


router = APIRouter()

@router.get("/folios")
def get_all(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.get_folios(db)


@router.post("/folios")
def create_folio(data: FolioCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.create_folio(data, db)


@router.get("/folios/{id}")
def get_folio(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.get_folio(id, db)

@router.put('/folios/{id}')
def update_folio(id: int, data: FolioUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.update_folio(id, data, db)


@router.delete("/folios/{id}")
def delete_folio(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.delete_folio(id, db)


@router.get("/folios/{id}/details")
def details(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return folio_controller.get_folio_details(id, db)


