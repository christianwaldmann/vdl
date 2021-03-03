from .base import UnitTest
from vdl.core.file_parser import FileParser


class TestFileParser(UnitTest):

    def setUp(self):
        UnitTest.setUp(self)
        self.filename = "testfile.txt"
        with open(self.filename, "w") as f:
            lines = ["1", "2", "3", "", "4"]
            f.writelines("%s\n" % l for l in lines)

    def test_GetNonEmptyLinesAsList_returns_correct_lines(self):
        fileParser = FileParser(self.filename)

        linesReadByParser = fileParser.GetNonEmptyLinesAsList()

        self.assertEqual(linesReadByParser, ["1\n", "2\n", "3\n", "4\n"])
