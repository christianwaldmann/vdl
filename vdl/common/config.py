from configparser import RawConfigParser
import os
from pathlib import Path


class BaseConfig(RawConfigParser):
    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), self.filename)
        )
        super(BaseConfig, self).__init__()
        self.Load()

    def Load(self):
        self.read(self.filepath)

    def Get(self, section, key, *args, **kwargs):
        return self.get(section, key, *args, **kwargs)

    def Set(self, section, key, value, persistent=True):
        self.set(section, key, value)
        if persistent:
            self._save()

    def _save(self):
        with open(self.filepath, "w") as configfile:
            self.write(configfile)


class Config(BaseConfig):
    def __init__(self, filename):
        super(Config, self).__init__(filename)

    def SetOutputDir(self, outputdir, **kwargs):
        self.Set("settings", "outputdir", outputdir, **kwargs)

    def GetOutputDir(self):
        defaultOutputDir = Path().home().joinpath("Downloads/idl")
        return self.Get("settings", "outputdir", raw=True, fallback=defaultOutputDir)

    def SetOutputTemplate(self, output_template, **kwargs):
        self.Set("ytdl_options", "outtmpl", output_template, **kwargs)

    def GetOutputTemplate(self):
        return self.Get("ytdl_options", "outtmpl")

    def SetRateLimit(self, rate_limit, **kwargs):
        self.Set("ytdl_options", "ratelimit", rate_limit * 1_000_000, **kwargs)

    def GetRateLimit(self):
        return self.Get("ytdl_options", "ratelimit")

    def GetAutoUpdate(self):
        return self.Get("settings", "auto_update")

    def SetAutoUpdate(self, active, **kwargs):
        return self.Set("settings", "auto_update", active, **kwargs)


s_Config = Config("../../config.ini")
