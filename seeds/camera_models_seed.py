import random
from faker import Faker

fake = Faker()

RESOLUTIONS = [
    (704, 576),
    (720, 576),
    (1280, 720),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160),
]

MANUFACTURERS = [
    "AXIS",
    "DAHUA",
    "Hikvision",
    "Bosch",
    "Hanwha",
    "360Vision",
    "Apix",
]

def generate_camera_model() -> dict:
    resolution_x, resolution_y = random.choice(RESOLUTIONS)

    max_real_zoom = random.choice([20, 30, 36, 45])
    max_virtual_zoom = random.choice([128, 9999, 30000])

    focus_min = round(random.uniform(2.5, 5.0), 1)
    focus_max = round(random.uniform(90, 180), 1)

    min_field_angle = round(random.uniform(15, 35), 1)
    max_field_angle = round(random.uniform(500, 700), 1)

    min_vertical_angle = 90
    max_vertical_angle = 15

    ptz = random.choice([0, 1])
    thermal = random.choice([0, 1])

    return {
        "manufacturer": random.choice(MANUFACTURERS),
        "model": f"{fake.word().upper()}-{random.randint(100, 9999)}",
        "resolutionX": resolution_x,
        "resolutionY": resolution_y,
        "maxVirtualZoom": max_virtual_zoom,
        "maxRealZoom": max_real_zoom,
        "focusMax": focus_max,
        "focusMin": focus_min,
        "MinFieldAngle": min_field_angle,
        "MaxFieldAngle": max_field_angle,
        "MinVerticalAngle": min_vertical_angle,
        "MaxVerticalAngle": max_vertical_angle,
        "streamDecFactor": random.choice([1, 2, 3]),
        "sectorLength": random.choice([12000, 15000, 20000, 28650]),
        "ptzCalculator": random.choice([0, 1]) if ptz else 0,
        "wiper": random.choice([0, 1]),
        "defog": random.choice([0, 1]),
        "stabilizer": random.choice([0, 1]),
        "ptz": ptz,
        "type": random.choice([0, 1, 2]),
        "invertPan": random.choice([0, 1]),
        "invertTilt": random.choice([0, 1]),
        "thermal": thermal,
        "snapshoter": random.choice([0, 1]),
    }

def generate_camera_models(count: int):
    return [generate_camera_model() for _ in range(count)]
