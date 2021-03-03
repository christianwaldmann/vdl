import os
import glob


def DownloadedVideoFileExists(filepath):
    if FileExists(filepath):
        return True
    else:
        return FileExists(GetCorrectFilepathInCaseOfYoutubeDLBug(filepath))


def FileExists(filepath):
    return os.path.isfile(filepath)


def GetCorrectFilepathInCaseOfYoutubeDLBug(filepath):
    # Handle youtube-dl bug: file extension of downloaded file is incorrect (doesnt match the specified value)
    # This happens because youtube-dl fetches the filename before downloading. The file extension of the
    # downloaded file may in some cases be incorrect. The code below attempts to fix this, but it's just a messy
    # workaround. There have been made several issues to youtube-dl, but no fix yet.
    # Reference: https://github.com/ytdl-org/youtube-dl/issues/5710
    if not FileExists(filepath):
        filepathAsMkv = ReplaceExtension(filepath, ".mkv")
        if FileExists(filepathAsMkv):
            return filepathAsMkv
    return filepath


def DirectoryContainsFilesWithExtension(directory, extension):
    path = os.path.join(directory, "*" + extension)
    if glob.glob(path):
        return True
    else:
        return False

def ReplaceExtension(filepath, newExtension):
    return os.path.splitext(filepath)[0] + newExtension


def CleanPath(filepath):
    return os.path.abspath(os.path.expanduser(filepath))