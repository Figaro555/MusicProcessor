from DB.Initializers.AbstractInitializer import AbstractInitializer


class YouTubeInitializer(AbstractInitializer):
    def create_tables(self, connection):
        try:
            connection.get_connection().set_session(autocommit=True)
            with connection.get_connection().cursor() as cursor:
                cursor.execute(open("DB/Initializers/YouTube/generate_tables.sql", "r").read())
        except Exception as _ex:
            print("[ERROR] Error while creating table with PostgreSQL", _ex)
