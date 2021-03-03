from .base import FunctionalTest
import subprocess



class TestInput(FunctionalTest):

    def test_displays_error_message_on_invalid_url(self):
        output = subprocess.check_output(['vdl', "hallo"], shell=True)

        self.wait_for(lambda: self.assertIn('"hallo" is an invalid or unsupported URL.', output.decode("utf8")))

