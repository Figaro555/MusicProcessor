from abc import ABC, abstractmethod


class AbstractDownloader(ABC):
    @abstractmethod
    def download_files(self, local_resource_path):
        pass
