# models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TestStudent(Base):
    __tablename__ = 'test_students'  # Создаем новую таблицу для тестов
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    
    def soft_delete(self):
        """Мягкое удаление студента"""
        self.is_active = False
        self.is_deleted = True
    
    def __repr__(self):
        return f"<TestStudent(id={self.id}, name='{self.name}', email='{self.email}')>"