from vdl.common.log import Log
from vdl.cli import CLI


def Main():
    Log.Init()
    cli = CLI()
    cli.Main()
