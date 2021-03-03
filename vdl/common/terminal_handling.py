import shutil
import contextlib
import io
import sys


@contextlib.contextmanager
def NoStdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout


@contextlib.contextmanager
def NoStderr():
    save_stderr = sys.stderr
    sys.stderr = io.BytesIO()
    yield
    sys.stderr = save_stderr


def ClearTerminalLineAndMoveCursorToStart():
    print((shutil.get_terminal_size().columns - 1) * " ", end="\r")
