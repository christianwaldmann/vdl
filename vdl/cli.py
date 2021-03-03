import argparse
import os
import pyperclip

from vdl.common.package_handling import PackageManager
from vdl.core.file_parser import FileParser
from vdl.common.config import s_Config
from vdl.common.url_handling import CleanUrl
from vdl.common.file_handling import CleanPath
from vdl.core.video_downloader import VideoDownloader


class CLI:
    def Main(self):
        args = self._ParseArgs()

        # Logic depending on parsed arguments
        if args.set_default_outputdir:
            s_Config.SetOutputDir(args.set_default_outputdir)

        if args.update or s_Config.GetAutoUpdate():
            packageManager = PackageManager()
            packageManager.Upgrade("youtube_dl")

        if args.url or args.batch_file or args.from_clipboard:
            # Preparation for download
            videoDownloader = VideoDownloader()
            output_template = CleanPath(os.path.join(
                args.output_dir, s_Config.GetOutputTemplate()
            ))
            s_Config.SetOutputTemplate(output_template, persistent=False)

            if args.batch_file:
                fileParser = FileParser(args.batch_file)
                for url in fileParser.GetNonEmptyLinesAsList():
                    videoDownloader.DownloadAndLog(CleanUrl(url))

            if args.from_clipboard:
                if args.file_name:
                    output_template = CleanPath(os.path.join(args.output_dir, args.file_name))
                    s_Config.SetOutputTemplate(output_template, persistent=False)
                videoDownloader.DownloadAndLog(CleanUrl(pyperclip.paste()))

            if args.url:
                if args.file_name:
                    output_template = CleanPath(os.path.join(args.output_dir, args.file_name))
                    s_Config.SetOutputTemplate(output_template, persistent=False)
                for url in args.url:
                    videoDownloader.DownloadAndLog(CleanUrl(url))

    def _ParseArgs(self):
        parser = argparse.ArgumentParser(description="vdl (video dl) - a cli to download videos")

        parser.add_argument("url", type=str, nargs="*", help="URL of the video to download")

        parser.add_argument(
            "-f",
            "--file-name",
            type=str,
            help="Specify filename (without extension) of the downloaded video file",
        )
        parser.add_argument(
            "-o",
            "--output-dir",
            type=str,
            help="Specify directory where the downloaded video file will be saved",
            default=s_Config.GetOutputDir(),
        )
        parser.add_argument(
            "-a",
            "--batch-file",
            type=str,
            help="Txt-file containing URLs to download, one URL per line",
        )
        parser.add_argument(
            "--from-clipboard",
            action="store_true",
            help="Get video URL to download from clipboard",
        )

        parser.add_argument(
            "--set-default-outputdir",
            type=str,
            help="Set default directory where downloaded videos will be saved, if no path is specified",
        )

        parser.add_argument(
            "--update",
            help="Update vdl and its dependencies",
            action="store_true",
        )
        return parser.parse_args()
