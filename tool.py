from datetime import datetime

def gaps(timestamps: list[str], expected_seconds: float) -> list[int]:
    points = [datetime.fromisoformat(value) for value in timestamps]
    return [index for index in range(1, len(points)) if (points[index] - points[index - 1]).total_seconds() > expected_seconds]
