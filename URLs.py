import gdown
import tarfile
import os

class URLs:
    @staticmethod
    def Download(url, destination, extract=False, delete_tar=True) -> str:
        final_destination:str = destination
        gdown.download(url, destination, quiet=False)
        if extract:
            tar = tarfile.open(destination, "r:gz")
            tar.extractall()
            final_destination = tar.getnames()
            tar.close()
            if (delete_tar):
                os.remove(destination)
        return final_destination

    @staticmethod
    def Hemnet() -> tuple:
        url:str = "https://drive.google.com/u/1/uc?id=1xXLhZaUryHoluEBmstBS-qCLu4vEbgw4&export=download"
        destination:str = "Hemnet.tar.gz"
        return url, destination