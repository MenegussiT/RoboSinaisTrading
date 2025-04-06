# tests/conftest.py ou no próprio test_crud_signal.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base  # Substitua pelo caminho correto


# Engine e sessão para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # ou sqlite:///:memory:
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Cria as tabelas no banco de teste
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Se quiser limpar após cada teste:
        Base.metadata.drop_all(bind=engine)

