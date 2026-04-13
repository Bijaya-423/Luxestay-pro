from sqlalchemy import Column, Integer, String, Float, String, ForeignKey
from app.models.base import BaseModel


class FolioItem(BaseModel):
    __tablename__ = "folio_items"


    folio_id = Column(Integer, ForeignKey("folios.id"))
    item_type = Column(String(50))
    description = Column(String(255))
    amount = Column(Float)

    # def __init__(self, folio_id, item_type, description, amount):
    #     self.folio_id = folio_id
    #     self.item_type = item_type
    #     self.description = description
    #     self.amount = amount

    # def __repr__(self):
    #     return f"<FolioItem {self.id}>"

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "folio_id": self.folio_id,
    #         "item_type": self.item_type,
    #         "description": self.description,
    #         "amount": self.amount,
    #     }


    