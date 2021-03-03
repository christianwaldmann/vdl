import os

from .base import FunctionalTest
from vdl.core.url_info_extractor import UrlInfoExtractor
from vdl.common.file_handling import DownloadedVideoFileExists


class TestDownload(FunctionalTest):

    def setUp(self):
        FunctionalTest.setUp(self)
        self.url1 = "https://www.youtube.com/watch?v=w0Cmuvu3qd0"
        self.url2 = "https://www.youtube.com/watch?v=OBF4kZS9baw"
        self.infoExtractor1 = UrlInfoExtractor(self.url1)
        self.infoExtractor2 = UrlInfoExtractor(self.url2)
        self.filepath1 = self.infoExtractor1.GetExpectedFilepath()
        self.filepath2 = self.infoExtractor2.GetExpectedFilepath()

    def test_can_download_video_from_youtube(self):
        self.assertFalse(DownloadedVideoFileExists(self.filepath1))

        os.system(f"vdl {self.url1} -o .")

        self.wait_for(lambda: self.assertTrue(DownloadedVideoFileExists(self.filepath1)))

    def test_can_download_multiple_videos_from_youtube_in_single_call(self):
        self.assertFalse(DownloadedVideoFileExists(self.filepath1))
        self.assertFalse(DownloadedVideoFileExists(self.filepath2))

        os.system(f"vdl {self.url1} {self.url2} -o .")


        self.wait_for(lambda: self.assertTrue(DownloadedVideoFileExists(self.filepath1)))
        self.wait_for(lambda: self.assertTrue(DownloadedVideoFileExists(self.filepath2)))

