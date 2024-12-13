from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class CarModel(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    capacit_motor = Column(Float, nullable=True)
    tip_combustibil = Column(String(50), nullable=True)
    anul_fabricatiei = Column(Integer, nullable=True)
    cutia_de_viteze = Column(String(50), nullable=True)
    marca = Column(String(100), nullable=True)
    modelul = Column(String(100), nullable=True)
    tip_tractiune = Column(String(50), nullable=True)
    distanta_parcursa = Column(Float, nullable=True)
    tip_caroserie = Column(String(50), nullable=True)
    price = Column(Float, nullable=True)
    link = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<Car(marca='{self.marca}', modelul='{self.modelul}', anul_fabricatiei={self.anul_fabricatiei})>"

    @classmethod
    def from_car_object(cls, car):
        """Convert a Car object to a CarModel instance"""
        return cls(
            capacit_motor=float(car.capacit_motor) if car.capacit_motor else None,
            tip_combustibil=car.tip_combustibil,
            anul_fabricatiei=int(car.anul_fabricatiei) if car.anul_fabricatiei else None,
            cutia_de_viteze=car.cutia_de_viteze,
            marca=car.marca,
            modelul=car.modelul,
            tip_tractiune=car.tip_tractiune,
            distanta_parcursa=float(car.distanta_parcursa) if car.distanta_parcursa else None,
            tip_caroserie=car.tip_caroserie,
            price=float(car.price) if car.price else None,
            link=car.link
        )

    def to_car_object(self):
        """Convert a CarModel instance to a Car object"""
        from car import Car  # Import here to avoid circular imports
        return Car(
            capacit_motor=str(self.capacit_motor) if self.capacit_motor else None,
            tip_combustibil=self.tip_combustibil,
            anul_fabricatiei=str(self.anul_fabricatiei) if self.anul_fabricatiei else None,
            cutia_de_viteze=self.cutia_de_viteze,
            marca=self.marca,
            modelul=self.modelul,
            tip_tractiune=self.tip_tractiune,
            distanta_parcursa=str(self.distanta_parcursa) if self.distanta_parcursa else None,
            tip_caroserie=self.tip_caroserie,
            price=str(self.price) if self.price else None,
            link=self.link
        )


# Database connection and session management
def init_db(database_url='sqlite:///cars.db'):
    """Initialize the database connection and create tables"""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


# Usage example:
if __name__ == '__main__':
    # Create a database session
    session = init_db()

    # Example of creating a new car entry
    # new_car = CarModel(marca='BMW', modelul='X5', anul_fabricatiei=2020)
    # session.add(new_car)
    # session.commit()