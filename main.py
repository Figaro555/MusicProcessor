from DB.KaggleTestOnDataDB.DBLoaderRDS import DBLoaderRDS
from DataLake.Loaders.S3Downloader import S3Downloader
from DataLake.Loaders.YouTubeDataDownloader import YouTubeDataDownloader
from DataLake.PseudoDataLake import PseudoDataLake
from Transformers.KaggleTestsOnDataTransformer import KaggleTestsOnDataTransformer
from Transformers.YouTubeDataTransformer import YouTubeDataTransformer


def main():
    pseudo_data_lake = PseudoDataLake([S3Downloader(), YouTubeDataDownloader()])
    print("[INFO] data was downloaded")

    local_dwh = {}
    for category, json_part in pseudo_data_lake.json_map.items():
        local_dwh[category] = (globals()[category+"Transformer"])().transform_to_local_array(json_part)

    print(local_dwh)


if __name__ == '__main__':
    main()
