from project.DB.DBManagers.KaggleDBManager import KaggleDBManager
from project.DB.DBManagers.YouTubeDBManager import YouTubeDBManager
from project.DataLake.DataLoaders.S3DataLoader import S3DataLoader
from project.DataLake.DataLoaders.YouTubeDataLoader import YouTubeDataLoader
from project.DataLake.PseudoDataLake import PseudoDataLake
from project.Transformers.Kaggle.TestsOnDataTransformer import TestsOnDataTransformer
from project.Transformers.YouTubeTransformer import YouTubeTransformer


def main():
    pseudo_data_lake = PseudoDataLake([YouTubeDataLoader(), S3DataLoader()])
    print("[INFO] data was downloaded")

    local_DWH = {
        "TestsOnData": TestsOnDataTransformer().transform_to_local_array(
            pseudo_data_lake.json_map["TestsOnData"]
        ),
        "YouTubeData": YouTubeTransformer().transform_to_local_array(pseudo_data_lake.json_map["YouTubeData"]["root"])
    }

    yt_manager = YouTubeDBManager()
    yt_manager.process_data(local_DWH["YouTubeData"])

    k_manager = KaggleDBManager()
    k_manager.process_data(local_DWH["TestsOnData"])


if __name__ == '__main__':
    main()
