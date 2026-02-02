from seeds import catalogs_forestries_seed
from sqlalchemy import create_engine, MetaData, Table, text

# ---- Настройка подключения ----
engine = create_engine("mysql+pymysql://test:test@127.0.0.1:3306/test_db")
metadata = MetaData()

with engine.begin() as conn:  # автоматически commit/rollback
    # Отражаем существующие таблицы
    metadata.reflect(bind=conn)
    catalogs_forestries_table = Table("catalogs_forestries", metadata, autoload_with=conn)

    # Генерация тестовых записей
    forestries = catalogs_forestries_seed.generate_forestries(5)

    # Вставка с конверсией WKT в GEOMETRY
    stmt = text("""
        INSERT INTO catalogs_forestries (name, code, code_lv, code_oiv, polygon)
        VALUES (:name, :code, :code_lv, :code_oiv, ST_GeomFromText(:polygon))
    """)

    conn.execute(stmt, forestries)

print("Данные успешно вставлены!")
