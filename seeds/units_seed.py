import random
import json

def generate_units(forestries_codes: list[int], count: int = 5):
    """
    Генерирует тестовые подразделения units.

    :param forestries_codes: список кодов forestries (int)
    :param count: сколько записей создать
    :return: список словарей для вставки
    """
    units = []

    for i in range(count):
        # Некоторые подразделения могут вообще не иметь forestries
        if random.random() < 0.2:
            unit_forestries = None
        else:
            # случайный поднабор forestries
            unit_forestries = random.sample(forestries_codes, k=random.randint(1, min(10, len(forestries_codes))))

        # Генерация defaultUserParams (как в твоем примере)
        default_params = {
            "userMonitoring": random.choice([True, False]),
            "userFires": random.choice([True, False]),
            "userTransport": random.choice([True, False]),
            "userDeforest": random.choice([True, False]),
            "userMapLayers": random.choice([True, False]),
            "mediaCollections": random.choice([True, False]),
            "userRecursions": random.choice([True, False]),
            "layersUnAccessible": {"base": ["osm"], "user": []},
            "workspace": "/view.php",
            "quadrator": random.randint(1, 20),
            "userExtRights": random.choice([True, False]),
            "userExtRightsHours": 24,
            "userRightsConfirmed": random.choice([True, False]),
            "canEditKPO": random.choice([True, False]),
            "canEditForestriesKPO": [],
        }

        unit = {
            "country": random.randint(1, 50),
            "region": random.randint(1, 50),
            "ordering": i + 1,
            "name": f"Подразделение {i+1}",
            "system": random.choice([0, 1]),
            "forestries": json.dumps(unit_forestries) if unit_forestries is not None else None,
            "defaultUserParams": json.dumps(default_params)
        }

        units.append(unit)

    return units
