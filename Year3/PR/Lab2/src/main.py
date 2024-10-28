from fastapi import FastAPI
from src.routes.car_routes import router as car_router
app = FastAPI(debug=True)

app.include_router(car_router)
