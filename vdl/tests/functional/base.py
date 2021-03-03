import unittest
import time
import os
import shutil


MAX_WAIT = 10


def wait(fn):
    """
    Explicit wait helper (for usage as decorator on functions)
    """

    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            # except (AssertionError) as e:
            except Exception as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.25)

    return modified_fn


class FunctionalTest(unittest.TestCase):
    def setUp(self):
        os.makedirs("./temp", exist_ok=True)
        os.chdir("./temp")

    def tearDown(self):
        os.chdir("..")
        shutil.rmtree("./temp")

    @wait
    def wait_for(self, fn):
        """
        Explicit wait helper (for inline usage)
        """
        return fn()
