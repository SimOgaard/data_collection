from pathlib import Path
import gdown

class URLs:
    @staticmethod
    def Download(url, destination, quiet=False):
        gdown.download(url, destination, quiet=quiet)

    @staticmethod
    def Hemnet() -> tuple:
        url:str = "https://drive.google.com/u/1/uc?id=1xXLhZaUryHoluEBmstBS-qCLu4vEbgw4&export=download"
        destination:str = "Hemnet.tar.gz"
        return url, destination