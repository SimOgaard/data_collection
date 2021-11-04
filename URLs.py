import gdown
import tarfile
import os

class URLs:
    @staticmethod
    def Download(url, destination, extract=False, delete_tar=True) -> str:
        ''' Downloads and extracts google drive url '''
        final_destination:str = destination
        gdown.download(url, destination, quiet=False)
        if extract:
            tar = tarfile.open(destination, "r:gz")
            tar.extractall()
            final_destination = tar.getnames()[0]
            tar.close()
            if (delete_tar):
                os.remove(destination)
        return final_destination

    @staticmethod
    def MountDrive() -> str:
        ''' Mounts your drive '''
        from google.colab import drive
        drive_directory:str = "/content/drive"
        drive.mount(drive_directory)
        return drive_directory
        
    @staticmethod
    def Upload(upload_file:str, upload_file_destination:str = "/MyDrive/data_collection"):
        ''' Tars local upload_file and uploads it to drive '''
        drive_directory = URLs.MountDrive()
        full_dir = drive_directory + upload_file_destination

        if not os.path.exists(full_dir):
            os.mkdir(full_dir)

        full_dir += "/" + upload_file.split("/")[-1].split(".")[0] + ".tar.gz"
        with tarfile.open(full_dir, "w:gz") as tar:
            tar.add(upload_file, arcname=os.path.basename(upload_file))

    @staticmethod
    def Hemnet() -> tuple:
        ''' Showcase of how you upload your dataset '''
        url:str = "https://drive.google.com/u/1/uc?id=1xXLhZaUryHoluEBmstBS-qCLu4vEbgw4&export=download"
        destination:str = "Hemnet.tar.gz"
        return url, destination

    @staticmethod
    def agNews() -> tuple:
        ''' Showcase of how you upload your dataset '''
        url:str = "https://drive.google.com/u/0/uc?id=1-1kd7EChNIM7O7W7zQGHtsKIQOaJer5a&export=download"
        destination:str = "aq_newsdataset.tar.gz"
        return url, destination

    @staticmethod
    def agNewsSentiment() -> tuple:
        ''' Showcase of how you upload your dataset '''
        url:str = "https://drive.google.com/u/1/uc?id=1SqpQLDNE4BqdA8M2cFuDBkNSci8BZ0Fv&export=download"
        destination:str = "ag_news_sentiment.tar.gz"
        return url, destination

    @staticmethod
    def gutenberg() -> tuple:
        ''' Showcase of how you upload your dataset '''
        url:str = "https://drive.google.com/u/0/uc?id=1--ekQM1VFScRrUdWyCU2p6BS7Jvp5Kth&export=download"
        destination:str = "gutenberg.tar.gz"
        return url, destination
    
    @staticmethod
    def gutenbergSentiment() -> tuple:
        ''' Showcase of how you upload your dataset '''
        url:str = "https://drive.google.com/u/1/uc?id=1picCONw6Jyg-0Bq6OsJjXG9OzyerLGBH&export=download"
        destination:str = "gutenberg_sentiment.tar.gz"
        return url, destination
