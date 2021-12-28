import os

from DBInitializers.TablesCreators.AthenaTablesCreator import AthenaTablesCreator
from project.Connectors.DB.AthenaConnector import AthenaConnector


def main():
    table_creator = AthenaTablesCreator()
    for root, dirs, files in os.walk("SQLFiles"):
        for file in files:
            if file.endswith(".ddl"):
                table_creator.create_tables(AthenaConnector(), [root + "/" + file])


if __name__ == '__main__':
    main()
