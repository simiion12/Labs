from uuid import UUID
from fastapi import APIRouter, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends, HTTPException, status
from typing import List

from src.models.schemas import CarCreate, CarUpdate
from src.models.models import car
from src.database.database import get_async_session


router = APIRouter(
    prefix="/car",
    tags=["car"],
)


@router.post("/", response_model=CarCreate, status_code=201)
async def create_car(car_create: CarCreate,
                     db: AsyncSession = Depends(get_async_session)):
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


@router.put("/{car_id}", response_model=CarUpdate)
async def update_car(car_id: UUID,
               car_update: CarUpdate,
               db: AsyncSession = Depends(get_async_session)):
    """Update car information"""
    query = select(car).where(car.c.id == car_id)
    result = await db.execute(query)
    existing_info = result.fetchone()

    if not existing_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {car_id} not found"
        )

    try:
        # Create the update statement
        update_car = car.update().where(car.c.id == car_id).values(
            capacit_motor=car_update.capacit_motor,
            tip_combustibil=car_update.tip_combustibil,
            anul_fabricatiei=car_update.anul_fabricatiei,
            cutia_de_viteze=car_update.cutia_de_viteze,
            marca=car_update.marca,
            modelul=car_update.modelul,
            tip_tractiune=car_update.tip_tractiune,
            distanta_parcursa=car_update.distanta_parcursa,
            tip_caroserie=car_update.tip_caroserie,
            price=car_update.price,
            link=car_update.link
        )

        # Execute the update
        await db.execute(update_car)
        await db.commit()
        return car_update
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.delete("/{car_id}", status_code=204)
async def delete_car(car_id: UUID,
                     db: AsyncSession = Depends(get_async_session)):
    """Delete car information"""
    query = select(car).where(car.c.id == car_id)
    result = await db.execute(query)
    existing_info = result.fetchone()

    if not existing_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {car_id} not found"
        )

    try:
        # Create the delete statement
        delete_car = car.delete().where(car.c.id == car_id)

        # Execute the delete
        await db.execute(delete_car)
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


@router.get("/{car_id}", response_model=CarCreate)
async def get_car(car_id: UUID,
                  db: AsyncSession = Depends(get_async_session)):
    """Get car information"""
    query = select(car).where(car.c.id == car_id)
    result = await db.execute(query)
    car_info = result.fetchone()

    if not car_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {car_id} not found"
        )

    return car_info


# @router.get("/", response_model=List[CarCreate])
# async def get_cars(
#         offset: int = Query(0, ge=0),  # Offset starts from 0, must be non-negative
#         limit: int = Query(10, ge=1, le=100), # Limit defaults to 10, between 1 and 100
#         db: AsyncSession = Depends(get_async_session)):
#     """
#     Get paginated list of cars
#
#     Parameters:
#     - offset: Number of items to skip (default 0)
#     - limit: Maximum number of items to return (default 10, max 100)
#
#     Returns:
#     List of cars
#     """
#     try:
#         # Create a query with offset and limit
#         query = select(car).offset(offset).limit(limit)
#
#         # Execute the query
#         result = await db.execute(query)
#         cars_list = result.fetchall()
#
#         # Check if no cars found
#         if not cars_list:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="No cars found"
#             )
#
#         return cars_list
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"An error occurred: {str(e)}"
#         )
#
#
# @router.get("/count")
# async def get_cars_count(db: AsyncSession = Depends(get_async_session)):
#     """
#     Get total number of cars in the database
#
#     Returns:
#     Total count of cars
#     """
#     try:
#         # Count total number of cars
#         query = select(car.c.id).count()
#         result = await db.execute(query)
#         count = result.scalar_one()
#
#         return {"total_cars": count}
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"An error occurred: {str(e)}"
#         )
#
