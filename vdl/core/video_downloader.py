import youtube_dl

from vdl.common.log import Log
from vdl.common.file_handling import DownloadedVideoFileExists, FileExists, GetCorrectFilepathInCaseOfYoutubeDLBug
from vdl.common.terminal_handling import ClearTerminalLineAndMoveCursorToStart, NoStderr
from vdl.core.youtube_dl_options import YoutubeDLOptions
from vdl.core.url_info_extractor import UrlInfoExtractor


class VideoDownloader:
    # TODO: refactor this function (probably move to application class which handles logging and downloading)
    def DownloadAndLog(self, url):
        try:
            print("Creating filename ...", end="\r")
            with NoStderr():
                infoExtractor = UrlInfoExtractor(url)
                filepath = infoExtractor.GetExpectedFilepath()
        except Exception as e:
            print(f'"{url}" is an invalid or unsupported URL.')
            Log.Info(f'"{url}" is an invalid or unsupported URL.')
            return

        ClearTerminalLineAndMoveCursorToStart()

        if not DownloadedVideoFileExists(filepath):
            try:
                Log.Info(f"Downloading {url}")
                self.Download(url, filepath)
                filepath = GetCorrectFilepathInCaseOfYoutubeDLBug(filepath)
                print(f'{filepath}')
                Log.Info(f'Download ended successfully. File: "{filepath}"')
            except Exception as e:
                print("An error occured")
                Log.Info(f"An error occured while downloading")
                return
        else:
            if not FileExists(filepath):
                filepath = GetCorrectFilepathInCaseOfYoutubeDLBug(filepath)
            print(f'File exists already. {filepath}')


    def Download(self, url, filepath):
        options = YoutubeDLOptions()
        options.SetFilepath(filepath)

        with youtube_dl.YoutubeDL(options.Get()) as ydl:
            ydl.download([url])


