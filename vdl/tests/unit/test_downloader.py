from .base import UnitTest
from vdl.core.url_info_extractor import UrlInfoExtractor
from vdl.core.video_downloader import VideoDownloader
from vdl.common.file_handling import DownloadedVideoFileExists


class TestDownload(UnitTest):
    def test_CanDownloadYoutubeVideo(self):
        url = "https://www.youtube.com/watch?v=OBF4kZS9baw"
        infoExtractor = UrlInfoExtractor(url)
        filepath = infoExtractor.GetExpectedFilepath()
        self.assertFalse(DownloadedVideoFileExists(filepath))

        videoDownloader = VideoDownloader()
        videoDownloader.Download(url, filepath)

        self.wait_for(
            lambda: self.assertTrue(DownloadedVideoFileExists(filepath))
        )
