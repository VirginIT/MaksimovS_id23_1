from fastapi import FastAPI
from app.db.database import Base, engine
from app.api import auth, image


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(image.router)


