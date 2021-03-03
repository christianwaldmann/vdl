from vdl.common.config import s_Config
from vdl.common.terminal_handling import ClearTerminalLineAndMoveCursorToStart


class YoutubeDLOptions:
    def __init__(self):
        # Get youtube-dl options from config
        self.data = dict(s_Config["ytdl_options"])

        # Add youtube-dl options that are always enabled (not exposed to config)
        self.data["quiet"] = True
        self.data["no_warnings"] = True
        self.data["progress_hooks"] = [self._DownloadHook]

    def Get(self):
        return self.data

    def SetFilepath(self, filepath):
        self.data["outtmpl"] = filepath

    def _DownloadHook(self, d):
        if d["status"] == "downloading":
            downloaded_megabytes = d["downloaded_bytes"] / 1000000
            try:
                total_megabytes = d["total_bytes"] / 1000000
            except KeyError:
                total_megabytes = d["total_bytes_estimate"] / 1000000
            arrow, spaces = self._ProgressBar(downloaded_megabytes, total_megabytes)
            try:
                speed_megabytes_per_sec = d["speed"] / 1000000
                print(
                    f"{downloaded_megabytes:.2f} / {total_megabytes:.2f} MB | {speed_megabytes_per_sec:.2f} MB/s | [{arrow}{spaces}] {d['_percent_str']}",
                    end="\r",
                )
            except:
                print(
                    f"{downloaded_megabytes:.2f} / {total_megabytes:.2f} MB | [{arrow}{spaces}] {d['_percent_str']}",
                    end="\r",
                )
        if d["status"] == "finished":
            ClearTerminalLineAndMoveCursorToStart()

    def _ProgressBar(self, current, total, barLength=30):
        percent = float(current) * 100 / total
        arrow = "█" * int(percent / 100 * barLength)
        spaces = " " * (barLength - len(arrow))
        return arrow, spaces
