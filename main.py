from DB.DBManagers.KaggleDBManager import KaggleDBManager
from DB.DBManagers.YouTubeDBManager import YouTubeDBManager
from DataLake.PseudoDataLake import PseudoDataLake
from Transformers.KaggleTestsOnDataTransformer import KaggleTestsOnDataTransformer
from Transformers.YouTubeTransformer import YouTubeTransformer


def main():
    # pseudo_data_lake = PseudoDataLake([S3Downloader(), YouTubeDownloader()])
    pseudo_data_lake = PseudoDataLake([])
    print("[INFO] data was downloaded")

    local_DWH = {
        "TestsOnData": KaggleTestsOnDataTransformer().transform_to_local_array(
            pseudo_data_lake.json_map["TestsOnData"]
        ),
        "YouTubeData": YouTubeTransformer().transform_to_local_array(pseudo_data_lake.json_map["YouTubeData"])
    }

    yt_manager = YouTubeDBManager()
    yt_manager.process_data(local_DWH["YouTubeData"])

    k_manager = KaggleDBManager()
    k_manager.process_data(local_DWH["TestsOnData"])




if __name__ == '__main__':
    main()
