import os
import youtube_dl

from vdl.common.config import s_Config
from vdl.core.youtube_dl_options import YoutubeDLOptions


class UrlInfoExtractor:

    def __init__(self, url):
        options = YoutubeDLOptions()
        with youtube_dl.YoutubeDL(options.Get()) as ydl:
            self.info = ydl.extract_info(url, download=False)
            self.filename = ydl.prepare_filename(self.info)

    def GetExpectedFilepath(self):
        filename = self.GetExpectedFilename()
        directory = os.path.abspath(os.path.dirname(s_Config.GetOutputTemplate()))
        filepath = os.path.join(directory, filename)
        return filepath

    def GetExpectedFilename(self):
        return self.filename

    def GetExtractor(self):
        return self.info["extractor"]