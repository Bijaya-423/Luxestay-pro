from sqlalchemy import Column, String, Boolean, Integer, BigInteger, String, Date, DateTime, Float#, Timestamp 
from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(191), nullable=True)
    email = Column(String(191), nullable=False, index=True)
    email_verified_at = Column(DateTime, nullable=True)

    password = Column(String(191), nullable=True)

    plan = Column(Integer, nullable=True)
    plan_expire_date = Column(Date, nullable=True)

    requested_plan = Column(Integer, default=0, nullable=False)
    trial_plan = Column(Integer, default=0, nullable=False)
    trial_expire_date = Column(Date, nullable=True)

    type = Column(String(100), nullable=True)

    storage_limit = Column(Float, default=0, nullable=False)

    avatar = Column(String(191), default="avatar.png", nullable=False)
    messenger_color = Column(String(191), default="#2180f3", nullable=False)

    lang = Column(String(100), nullable=True)
    default_pipeline = Column(Integer, nullable=True)

    active_status = Column(Integer, default=0, nullable=False)
    delete_status = Column(Integer, default=1, nullable=False)

    mode = Column(String(10), default="light", nullable=False)
    dark_mode = Column(Integer, default=0, nullable=False)

    is_disable = Column(Integer, default=1, nullable=False)
    is_enable_login = Column(Integer, default=1, nullable=False)
    is_active = Column(Integer, default=1, nullable=False)

    referral_code = Column(Integer, default=0, nullable=False)
    used_referral_code = Column(Integer, default=0, nullable=False)
    commission_amount = Column(Integer, default=0, nullable=False)

    last_login_at = Column(DateTime, nullable=True)

    created_by = Column(Integer, default=0, nullable=False)

    remember_token = Column(String(100), nullable=True)

    # created_at = Column(Timestamp, nullable=True)
    # updated_at = Column(Timestamp, nullable=True)

    is_email_verified = Column(Integer, default=0, nullable=False)