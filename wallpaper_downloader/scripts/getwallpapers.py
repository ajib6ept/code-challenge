from wallpaper_downloader.cli import arg_parse
from wallpaper_downloader.downloader import download


def main() -> None:
    args = arg_parse()
    download(*args)
