CURRENT_WEATHER_SCHEMA = {
    "type": "object",
    "properties": {
        "coord": {
            "properties": {
                "lon": {"type": "number"},
                "lat": {"type": "number"}
            }
        },
        "weather": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "main": {"type": "string"},
                    "description": {"type": "string"},
                    "icon": {"type": "string"}
                }
            }
        },
        "base": {"type": "string"},
        "main": {
            "type": "object",
            "items": {
                "type": "object",
                "properties": {
                    "temp": {"type": "number"},
                    "feels_like": {"type": "number"},
                    "temp_min": {"type": "number"},
                    "temp_max": {"type": "number"},
                    "pressure": {"type": "number"},
                    "humidity": {"type": "number"}
                }
            }
        },
        "wind": {
            "type": "object",
            "items": {
                "type": "object",
                "properties": {
                    "speed": {"type": "number"},
                    "deg": {"type": "number"},
                }
            }
        },
        "clouds": {
            "type": "object",
            "items": {
                "type": "object",
                "properties": {
                    "all": {"type": "number"},
                }
            }
        },
        "dt": {"type": "number"},
        "sys": {
            "type": "object",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "integer"},
                    "id": {"type": "integer"},
                    "message": {"type": "number"},
                    "country": {"type": "string"},
                    "sunrise": {"type": "number"},
                    "sunset": {"type": "number"}
                }
            }
        },
        "timezone": {"type": "number"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "cod": {"type": "integer"},
    }
}
