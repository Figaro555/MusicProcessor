from DBInitializers.TablesCreators.AbstaractTablesCreator import AbstractTablesCreator


class AthenaTablesCreator(AbstractTablesCreator):
        def create_tables(self, connection, files_to_execute):
            for file_to_execute in files_to_execute:
                try:
                    connection.get_connection().start_query_execution(
                        QueryString=open(file_to_execute).read(),
                        ResultConfiguration={'OutputLocation': 's3://myprojectbucket111/Athena/queries/'})
                except Exception as _ex:
                    print("[ERROR] Error while running " + file_to_execute, _ex)
