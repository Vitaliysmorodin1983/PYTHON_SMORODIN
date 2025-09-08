# check_table_structure.py
from sqlalchemy import create_engine, text

def check_student_table():
    try:
        DB_URL = "postgresql://postgres:1234@localhost:5432/postgres"
        engine = create_engine(DB_URL)
        
        with engine.connect() as conn:
            # Проверяем структуру таблицы student
            result = conn.execute(text("""
                SELECT column_name, data_type, is_nullable 
                FROM information_schema.columns 
                WHERE table_name = 'student' 
                ORDER BY ordinal_position;
            """))
            
            print("Структура таблицы 'student':")
            print("-----------------------------------")
            for row in result:
                print(f"{row[0]:15} {row[1]:20} {row[2]}")
            print("-----------------------------------")
            
            # Проверяем существующие записи
            result = conn.execute(text("SELECT COUNT(*) FROM student;"))
            count = result.scalar()
            print(f"Количество записей в таблице: {count}")
            
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    check_student_table()