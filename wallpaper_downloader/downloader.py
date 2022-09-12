import logging
import os
import shutil
from datetime import datetime
from typing import List, cast

import lxml.html
import requests

from wallpaper_downloader.logger import create_logger

BASE_URL = "https://www.smashingmagazine.com"

IMAGE_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images"
)


def download(img_date: str, img_resolution: str, loglevel: str) -> None:
    create_logger(loglevel)
    mk_dir(IMAGE_FOLDER)
    page_url = create_url(img_date)
    html = download_page(page_url)
    image_urls = get_image_urls_from_html(html, img_resolution)
    for url in image_urls:
        download_image(url, IMAGE_FOLDER)


def download_page(url: str) -> str:
    r = requests.get(
        url,
        allow_redirects=False,
        timeout=5,
    )
    r.raise_for_status()
    return r.content.decode("utf-8")


def download_image(url: str, save_path: str) -> None:
    filename = url.split("/")[-1]
    path = os.path.join(save_path, filename)
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(path, "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


def get_image_urls_from_html(html: str, img_resolution: str) -> List[str]:
    html_xml = lxml.html.fromstring(html)
    urls = cast(
        List[str], html_xml.xpath(f'//a[text()="{img_resolution}"]/@href')
    )
    return urls


def create_url(month_year: str, base_url: str = BASE_URL) -> str:
    """
    >>> create_url('072017')
    'https://www.smashingmagazine.com/2017/06/desktop-wallpaper-calendars-july-2017/'
    """

    month, year = month_year[:2], month_year[2:]
    previous_month = str(int(month) - 1).zfill(2)
    current_year = year
    if previous_month == "00":
        year = cast(str, int(year) - 1)
        previous_month = "12"
    month_name = datetime.strptime(month, "%m").strftime("%B").lower()
    new_url = f"{base_url}/{year}/{previous_month}/desktop-wallpaper-calendars-{month_name}-{current_year}/"  # noqa: E501
    return new_url


def mk_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"{path} directory was created")
