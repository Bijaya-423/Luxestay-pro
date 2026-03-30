from pydantic import BaseModel


class RoomStatusUpdate(BaseModel):
    status: str

    # class Config:
    #     orm_mode = True


# class RoomStatusResponse(BaseModel):
#     room_number: str
#     status: str

#     class Config:
#         orm_mode = True


# class RoomStatusListResponse(BaseModel):
#     rooms: list[RoomStatusResponse]
