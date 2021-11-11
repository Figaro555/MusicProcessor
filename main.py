from PseudoDataLake import PseudoDataLake


from config import host, user, password, db_name, port
import psycopg2


def main():
    pseudo_data_lake = PseudoDataLake()

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port

        )
        cursor = connection.cursor()
        print(connection.commit())

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    main()
