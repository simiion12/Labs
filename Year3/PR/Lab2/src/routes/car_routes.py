from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from src.models.schemas import CarCreate, CarUpdate
from src.models.models import car
from src.database.database import get_async_session


router = APIRouter(
    prefix="/car",
    tags=["car"],
)


@router.post("/create", response_model=CarCreate, status_code=201)
async def create_car(car_create: CarCreate, db: AsyncSession = Depends(get_async_session)):
    try:
        # Create the insert statement
        new_car = car.insert().values(
            capacit_motor=car_create.capacit_motor,
            tip_combustibil=car_create.tip_combustibil,
            anul_fabricatiei=car_create.anul_fabricatiei,
            cutia_de_viteze=car_create.cutia_de_viteze,
            marca=car_create.marca,
            modelul=car_create.modelul,
            tip_tractiune=car_create.tip_tractiune,
            distanta_parcursa=car_create.distanta_parcursa,
            tip_caroserie=car_create.tip_caroserie,
            price=car_create.price,
            link=car_create.link
        )

        # Execute the insert
        await db.execute(new_car)
        await db.commit()
        return car_create
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )