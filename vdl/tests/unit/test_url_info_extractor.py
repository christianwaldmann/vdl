from .base import UnitTest
from vdl.core.url_info_extractor import UrlInfoExtractor


class TestUrlInfoExtractor(UnitTest):

    def test_RetrieveCorrectFilenameFromUrl(self):
        extractor = UrlInfoExtractor("https://www.youtube.com/watch?v=w0Cmuvu3qd0")

        filename = extractor.GetExpectedFilename()

        self.assertEqual(filename, "Test video 5 seconds of fireworks_w0Cmuvu3qd0.mp4")