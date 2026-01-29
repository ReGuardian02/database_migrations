from seeds import camera_models_seed
from sqlalchemy import create_engine, MetaData, Table

# Подключение к локальной тестовой БД
engine = create_engine("mysql+pymysql://test:test@127.0.0.1:3306/test_db")
# Создаём объект MetaData
metadata = MetaData()

# Подключение к БД и отражение существующих таблиц
with engine.connect() as conn:
    metadata.reflect(bind=conn)  # bind передаём в reflect
    camera_models_table = Table("camera_models", metadata, autoload_with=conn)

    # Генерация тестовых моделей
    models = camera_models_seed.generate_camera_models(50)

    # Вставка
    conn.execute(camera_models_table.insert(), models)
    conn.commit()