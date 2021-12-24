from datetime import time

from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator


class TimeSerializator(AbstractDataSerializator):
    def serialize(self, date):
        time_info = time.strftime("%X", time.localtime(date)).split('/')
        return {"id": round(date), "hour": time_info[0], "minute": time_info[1], "second": time_info[2]}
