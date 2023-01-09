from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credtials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credtials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")

    if not utils.verify(user_credtials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    return {"token": "example token"}