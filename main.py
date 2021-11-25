from DB.KaggleTestOnDataDB.KaggleTestOnDataLoaderRDS import KaggleTestOnDataLoaderRDS
from DB.YouTubeDB.YouTubeLoaderRDS import YouTubeLoaderRDS
from DataLake.Loaders.S3Downloader import S3Downloader
from DataLake.Loaders.YouTubeDownloader import YouTubeDownloader
from DataLake.PseudoDataLake import PseudoDataLake
from Transformers.KaggleTestsOnDataTransformer import KaggleTestsOnDataTransformer
from Transformers.YouTubeTransformer import YouTubeTransformer


def main():
    pseudo_data_lake = PseudoDataLake([S3Downloader(), YouTubeDownloader()])
    print("[INFO] data was downloaded")

    local_DWH = {
        "KaggleTestsOnData": KaggleTestsOnDataTransformer().transform_to_local_array(
            pseudo_data_lake.json_map["KaggleTestsOnData"]
        ),
        "YouTubeData": YouTubeTransformer().transform_to_local_array(pseudo_data_lake.json_map["YouTubeData"])
    }

    try:
        dbl = KaggleTestOnDataLoaderRDS(local_DWH["KaggleTestsOnData"])
        dbl.load()
    except Exception as _ex:
        print("[ERROR] Error while connection with PostgreSQL", _ex)
    finally:
        if dbl.connection:
            dbl.connection.close()
    try:
        dbl2 = YouTubeLoaderRDS(local_DWH["YouTubeData"])
        dbl2.load()

    except Exception as _ex:
        print("[ERROR] Error while connection with PostgreSQL", _ex)
    finally:
        if dbl2.connection:
            dbl2.connection.close()


if __name__ == '__main__':
    main()
