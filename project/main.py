from project.DB.DBManagers.KaggleDBManager import KaggleDBManager
from project.DB.DBManagers.YouTubeDBManager import YouTubeDBManager
from project.DataLake.DataSavers.S3DataSaver import S3DataSaver
from project.DataLake.DataSavers.YouTubeDataSaver import YouTubeDataSaver
from project.DataLake.PseudoDataLake import PseudoDataLake
from project.Transformers.KaggleTestsOnDataTransformer import KaggleTestsOnDataTransformer
from project.Transformers.YouTubeTransformer import YouTubeTransformer


def main():
    pseudo_data_lake = PseudoDataLake([YouTubeDataSaver(), S3DataSaver()])
    print("[INFO] data was downloaded")

    local_DWH = {
        "TestsOnData": KaggleTestsOnDataTransformer().transform_to_local_array(
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
