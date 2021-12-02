import os

from DBInitializers.TablesCreators.PostgresTablesCreator import PostgresTablesCreator
from project.Connectors.DB.PostgresConnector import PostgresConnector


def main():
    table_creator = PostgresTablesCreator()
    for root, dirs, files in os.walk("SQLFiles"):
        for file in files:
            if file.endswith(".sql"):
                table_creator.create_tables(PostgresConnector(), [root + "/" + file])


if __name__ == '__main__':
    main()
