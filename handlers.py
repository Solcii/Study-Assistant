from datetime import datetime


def get_day():
    today = datetime.now()
    format = today.strftime('%d/%m/%Y')
    return format

