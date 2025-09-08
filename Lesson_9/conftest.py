# conftest.py
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, TestStudent

DB_URL = "postgresql://postgres:1234@localhost:5432/postgres"

@pytest.fixture(scope="session")
def engine():
    """Фикстура для создания движка БД"""
    engine = create_engine(DB_URL)
    return engine

@pytest.fixture(scope="session")
def setup_test_tables(engine):
    """Создаем тестовые таблицы и удаляем старые"""
    # Удаляем тестовую таблицу если существует (используем text())
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS test_students CASCADE;"))
        conn.commit()
    
    # Создаем новую тестовую таблицу
    Base.metadata.create_all(engine)
    yield
    
    # Удаляем тестовую таблицу после тестов
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS test_students CASCADE;"))
        conn.commit()

@pytest.fixture
def db_session(engine, setup_test_tables):
    """Фикстура для создания сессии БД"""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session
    
    # Откатываем транзакцию после каждого теста
    session.rollback()
    session.close()
    connection.close()