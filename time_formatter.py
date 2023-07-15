import json

def format_time(duration):
    days = duration // (24 * 60)
    hours = (duration % (24 * 60)) // 60
    minutes = (duration % (24 * 60)) % 60

    formatted_time = ""
    if days > 0:
        formatted_time += f"{days}d "
    if hours > 0:
        formatted_time += f"{hours}h "
    if minutes > 0 or (days == 0 and hours == 0):
        formatted_time += f"{minutes}m"

    return formatted_time.strip()