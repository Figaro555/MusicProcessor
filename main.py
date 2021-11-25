from DB.KaggleTestOnDataDB.DBLoaderRDS import DBLoaderRDS
from DataLake.Loaders.S3Downloader import S3Downloader
from DataLake.Loaders.YouTubeDownloader import YouTubeDownloader
from DataLake.PseudoDataLake import PseudoDataLake
from Transformers.KaggleTestsOnDataTransformer import KaggleTestsOnDataTransformer
from Transformers.YouTubeTransformer import YouTubeTransformer


def main():
    pseudo_data_lake = PseudoDataLake([S3Downloader(), YouTubeDownloader()])
    local_pseudo_data_warehouse = []
    print("[INFO] data was downloaded")

    local_DWH = {"KaggleTestsOnData": KaggleTestsOnDataTransformer().transform_to_local_array(
        pseudo_data_lake.json_map["KaggleTestsOnData"]),
        "YouTubeData": YouTubeTransformer().transform_to_local_array(pseudo_data_lake.json_map["YouTubeData"])}

    try:
        dbl = DBLoaderRDS(local_pseudo_data_warehouse)
        dbl.create_tables()
        dbl.load()
    except Exception as _ex:
        print("[ERROR] Error while working with PostgreSQL", _ex)
    finally:
        if dbl.connection:
            dbl.connection.close()


if __name__ == '__main__':
    main()
