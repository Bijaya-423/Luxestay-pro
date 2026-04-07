from sqlalchemy import Column, Integer, String, Date, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    name = Column(String(100), nullable=True)
    dob = Column(Date, nullable=True)
    gender = Column(String(10), nullable=True)
    phone = Column(String(15), nullable=True)
    address = Column(String(255), nullable=True)
    email = Column(String(100), nullable=True)
    password = Column(String(255), nullable=True)
    employee_id = Column(String(50), nullable=True)
    biometric_emp_id = Column(JSON, nullable=True)
    branch_id = Column(Integer, nullable=True)
    department_id = Column(Integer, default=0)
    designation_id = Column(Integer, nullable=True)
    company_doj = Column(String(191), nullable=True)
    documents = Column(String(191), nullable=True)

    account_holder_name = Column(String(191), nullable=True)
    account_number = Column(String(191), nullable=True)
    bank_name = Column(String(191), nullable=True)
    bank_identifier_code = Column(String(191), nullable=True)
    branch_location = Column(String(191), nullable=True)
    tax_payer_id = Column(String(191), nullable=True)

    account = Column(Integer, nullable=True)

    salary_type = Column(Integer, nullable=True)
    salary = Column(Integer, nullable=True)

    is_active = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    aadhaar_number = Column(String(12), nullable=True)
    employee_type = Column(String(50), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    rejoin_reason = Column(String, nullable=True)

    uan_number = Column(String(20), nullable=True)
    ip_number = Column(String(20), nullable=True)

    
    father_name = Column(String(255), nullable=True)
    skills = Column(String(255), default="Unskills")