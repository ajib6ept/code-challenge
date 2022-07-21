from datetime import datetime

import click

from wallpaper_downloader.downloader import download_images

MIN_DATE = "072008"
MAX_DATE = datetime.today().strftime("%m%Y")

FILE_RESOLUTION_OPTIONS = (
    "320x480",
    "640x480",
    "800x480",
    "800x600",
    "1024x768",
    "1024x1024",
    "1152x864",
    "1280x720",
    "1280x960",
    "1280x1024",
    "1366x768",
    "1400x1050",
    "1440x900",
    "1600x1200",
    "1680x1050",
    "1680x1200",
    "1920x1080",
    "1920x1200",
    "1920x1440",
    "2560x1440",
)


def validate_image_date(ctx, param, value):
    try:
        dt = datetime.strptime(value, "%m%Y")
    except ValueError:
        raise click.BadParameter(
            "please specify the correct format, for example 022018"
        )
    min_date_dt = datetime.strptime(MIN_DATE, "%m%Y")
    max_date_dt = datetime.strptime(MAX_DATE, "%m%Y")
    if dt < min_date_dt or dt > max_date_dt:
        raise click.BadParameter(
            f"please specify the correct format, from {MIN_DATE} to {MAX_DATE}"
        )
    return value


def validate_image_resolution(ctx, param, value):
    if value not in FILE_RESOLUTION_OPTIONS:
        raise click.BadParameter(
            "please specify the correct format, for example 640x480"
        )
    return value


@click.command()
@click.help_option("-h", "--help")
@click.option(
    "-l",
    "--loglevel",
    default="INFO",
    help="tool loglevel: DEBUG, INFO or WARN (default: INFO)",
    type=click.Choice(["DEBUG", "INFO", "WARN"], case_sensitive=False),
)
@click.argument("image_date", callback=validate_image_date)
@click.argument("image_resolution", callback=validate_image_resolution)
def arg_parse(image_date, image_resolution, loglevel):
    download_images(image_date, image_resolution, loglevel)
