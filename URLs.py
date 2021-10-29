from pathlib import Path
import gdown

class URLs:
    @staticmethod
    def Download(url, destination):
        gdown.download(url, destination)

    @staticmethod
    def Hemnet() -> tuple:
        url:str = "https://drive.google.com/u/1/uc?id=1xXLhZaUryHoluEBmstBS-qCLu4vEbgw4&export=download"
        destination:str = "Hemnet.tar.gz"
        return url, destination