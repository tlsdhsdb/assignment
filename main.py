from fastapi import FastAPI
from controller.trademark_controller import router as trademark_router

app = FastAPI()
app.include_router(trademark_router,prefix="/trademark")