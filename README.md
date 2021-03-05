# vdl
vdl is a command line interface for downloading videos from Youtube.com and other sites.

It's build on top of youtube-dl and focuses on easier usage for common use cases.
It requires the Python interpreter and is not platform specific.

## Key Features
- Simple Interface to download videos
- Default download location customizable via config file, aswell as ability to specify output directory and filename directly
- Customize default youtube-dl options via config file
- Download urls from batch file
- Update dependencies (youtube-dl) easily manually or automatically if option `auto_update` in config is set to `True`

## Usage

````
vdl [OPTIONS] URL [ADDITIONAL URLS]
````

### Options

````
  -h, --help            show this help message and exit
  -f FILE_NAME, --file-name FILE_NAME
                        Specify filename (without extension) of the downloaded
                        video file
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Specify directory where the downloaded video file will
                        be saved
  -a BATCH_FILE, --batch-file BATCH_FILE
                        Txt-file containing URLs to download, one URL per line
  --from-clipboard      Get video URL to download from clipboard
  -r LIMIT_RATE, --limit-rate LIMIT_RATE
                        Maximum download rate in MB/s
  --set-default-outputdir SET_DEFAULT_OUTPUTDIR
                        Set default directory where downloaded videos will be
                        saved, if no path is specified
  --update              Update vdl and its dependencies
````

## Default Configuration
config.ini
````
[settings]
outputdir = ~/Downloads/vdl
auto_update = False

[ytdl_options]
format = (bestvideo[width>=1920]/bestvideo)+bestaudio/best
outtmpl = %(title)s_%(id)s.%(ext)s
prefer_ffmpeg = True
cachedir = False
noplaylist = True
````

## Examples

#### Download video
````
vdl https://www.youtube.com/watch?v=dQw4w9WgXcQ
````

#### Download video to current folder
````
vdl https://www.youtube.com/watch?v=dQw4w9WgXcQ -o .
````

#### Download video to specified folder
````
vdl https://www.youtube.com/watch?v=dQw4w9WgXcQ -o C:\Downloads
````

#### Download multiple videos
````
vdl https://www.youtube.com/watch?v=dQw4w9WgXcQ https://www.youtube.com/watch?v=2ocykBzWDiM
````

#### Download videos from txt-file containing urls
````
vdl -a urls.txt
````


## For Developers
### Testing
To manually run all tests (unit and functional tests): `python -m unittest discover vdl/tests`
