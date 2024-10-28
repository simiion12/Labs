from typing import Optional
from pydantic import BaseModel, Field


class CarCreate(BaseModel):
    capacit_motor: str
    tip_combustibil: str
    anul_fabricatiei: str
    cutia_de_viteze: str
    marca: str
    modelul: str
    tip_tractiune: str
    distanta_parcursa: str
    tip_caroserie: str
    price: str
    link: str


class CarUpdate(BaseModel):
    capacit_motor: Optional[str] = None
    tip_combustibil: Optional[str] = None
    anul_fabricatiei: Optional[str] = None
    cutia_de_viteze: Optional[str] = None
    marca: Optional[str] = None
    modelul: Optional[str] = None
    tip_tractiune: Optional[str] = None
    distanta_parcursa: Optional[str] = None
    tip_caroserie: Optional[str] = None
    price: Optional[str] = None
    link: Optional[str] = None
