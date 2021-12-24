from datetime import time

from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator


class DateSerializator(AbstractDataSerializator):
    def serialize(self, date):
        date_info = time.strftime("%x", time.localtime(date)).split('/')
        return {"id": round(date), "day": date_info[1], "month": date_info[0], "year": date_info[2]}
