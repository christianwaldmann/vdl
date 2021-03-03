from .base import UnitTest
from vdl.common.config import s_Config
from vdl.common.file_handling import FileExists


class TestConfig(UnitTest):

    def test_FileExists(self):
        filepath = s_Config.filepath

        self.assertTrue(FileExists(filepath))

    def test_ContainsExpectedSections(self):
        s_Config.Load()

        self.assertIn("settings", s_Config.sections())
        self.assertIn("ytdl_options", s_Config.sections())

    def test_CanChangeDefaultOutputDir(self):
        previous_outputdir = s_Config.GetOutputDir()
        new_outputdir = "test-outputdir"
        self.assertNotEqual(previous_outputdir, new_outputdir)

        s_Config.SetOutputDir(new_outputdir)

        self.assertEqual(new_outputdir, s_Config.GetOutputDir())
        # Revert to original state
        s_Config.SetOutputDir(previous_outputdir)

