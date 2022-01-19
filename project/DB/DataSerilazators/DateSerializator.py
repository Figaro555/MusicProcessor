import time

from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator


class DateSerializator(AbstractDataSerializator):
    def serialize(self, date):
        date_info = time.strftime("%x", time.localtime(date)).split('/')
        return {"id": round(date), "day": int(date_info[1]), "month": int(date_info[0]), "year": int(date_info[2])}
