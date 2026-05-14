from fastapi import HTTPException
from app.models.permission import Permission
from app.models.role_permission import RolePermission


def create_permission(data, db):
    existing = db.query(Permission).filter(Permission.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Permission already exists")

    obj = Permission(name=data.name, created_by=1)

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj



def get_permissions(db):
    return db.query(Permission).all()


def get_permission(id, db):
    obj = db.query(Permission).filter(Permission.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Permission not found")

    return obj


def update_permission(id, data, db):
    obj = db.query(Permission).filter(Permission.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Permission not found.")

    obj.name = data.name

    db.commit()
    db.refresh(obj)

    return obj


def delete_permission(id, db):
    obj = db.query(Permission).filter(Permission.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Permission Not Found.")

    db.delete(obj)
    db.commit()
    return {"Message": "Deleted Successfully."}


def assign_permission_to_role(role_id, permission_ids, db):
    db.query(RolePermission).filter(RolePermission.role_id == role_id).delete()

    for pid in permission_ids:
        obj = RolePermission(role_id=role_id, permission_id=pid)
        db.add(obj)

    db.commit()
    return {"message": "Permissions assigned to role."}
    

def get_role_permissions(role_id, db):
    permissions = db.query(RolePermission).filter(RolePermission.role_id == role_id).all()
    return Permissions

def update_role_permissions(role_id, permission_ids, db):
    #remove the old permissions
    db.query(RolePermission).filter(RolePermission.role_id == role_id).delete()

    #add new permissions
    for pid in permission_ids:
        obj = RolePermission(role_id=role_id, permission_id=pid)
        db.add(obj)
    
    db.commit()
    return {"message": "Permissions updated successfully."}

def delete_role_permission(role_id, db):
    permissions = db.query(RolePermission).filter(RolePermission.role_id == role_id).all()

    if not permissions:
        raise HTTPException(status_code=404, detail="No permissions found.")
    
    db.query(RolePermission).filter(RolePermission.role_id == role_id).delete()

    # for permission in permissions:
    #     db.delete(permission)
    db.commit()
    return {"message": "Role permissions deleted successfully."}
