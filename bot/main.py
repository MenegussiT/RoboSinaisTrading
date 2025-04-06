from database.db import Base, engine
from database import models


def init_db():
    Base.metadata.create_all(bind=engine)


def main():
    init_db()
    print("Banco de dados inicializado com sucesso!")


if __name__ == "__main__":
    main()