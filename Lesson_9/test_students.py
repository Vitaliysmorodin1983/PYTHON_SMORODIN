# test_students.py
import pytest
from models import TestStudent

def test_create_student(db_session):
    """Тест создания студента"""
    # Arrange
    new_student = TestStudent(
        name="Иван Петров",
        email="ivan.petrov@example.com"
    )
    
    # Act
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)
    
    # Assert
    assert new_student.id is not None
    assert new_student.name == "Иван Петров"
    assert new_student.email == "ivan.petrov@example.com"
    assert new_student.is_active is True
    assert new_student.is_deleted is False
    print("✓ Тест создания студента пройден")

def test_update_student(db_session):
    """Тест обновления данных студента"""
    # Arrange - создаем студента
    student = TestStudent(
        name="Мария Сидорова",
        email="maria.sidorova@example.com"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    
    # Act - обновляем email
    original_id = student.id
    student.email = "maria.new@example.com"
    db_session.commit()
    db_session.refresh(student)
    
    # Assert - проверяем изменения
    assert student.id == original_id
    assert student.email == "maria.new@example.com"
    assert student.name == "Мария Сидорова"
    print("✓ Тест обновления студента пройден")

def test_soft_delete_student(db_session):
    """Тест мягкого удаления студента"""
    # Arrange - создаем студента
    student = TestStudent(
        name="Алексей Иванов",
        email="alexey.ivanov@example.com"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    
    # Act - выполняем мягкое удаление
    original_id = student.id
    student.soft_delete()
    db_session.commit()
    db_session.refresh(student)
    
    # Assert - проверяем флаги удаления
    assert student.id == original_id
    assert student.is_active is False
    assert student.is_deleted is True
    print("✓ Тест мягкого удаления студента пройден")