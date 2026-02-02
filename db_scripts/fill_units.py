from seeds import units_seed
from sqlalchemy import create_engine, MetaData, Table, text

# Подключение к локальной тестовой БД
engine = create_engine("mysql+pymysql://test:test@127.0.0.1:3306/test_db")
metadata = MetaData()

with engine.connect() as conn:
    metadata.reflect(bind=conn)
    units_table = Table("units", metadata, autoload_with=conn)

    # Берём все коды forestries
    result = conn.execute(text("SELECT code FROM catalogs_forestries"))
    forestries_codes = [int(row[0]) for row in result]

    # Генерация тестовых подразделений
    units = units_seed.generate_units(forestries_codes, 10)

    # Вставка
    conn.execute(units_table.insert(), units)
    conn.commit()


print("Подразделения успешно вставлены!")
