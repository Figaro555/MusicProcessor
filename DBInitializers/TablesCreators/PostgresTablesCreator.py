from DBInitializers.TablesCreators.AbstaractTablesCreator import AbstractTablesCreator


class PostgresTablesCreator(AbstractTablesCreator):
    def create_tables(self, connection, files_to_execute):
        for file_to_execute in files_to_execute:
            try:
                connection.get_connection().set_session(autocommit=True)
                with connection.get_connection().cursor() as cursor:
                    cursor.execute(open(file_to_execute, "r").read())
            except Exception as _ex:
                print("[ERROR] Error while running " + file_to_execute, _ex)


