import os
import shutil
from datetime import datetime

import lxml.html
import requests

BASE_URL = "https://www.smashingmagazine.com"

IMAGE_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images"
)


def download_images(img_date, img_resolution, loglevel):
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)
    page_url = create_url(BASE_URL, img_date)
    html = download_page(page_url)
    image_urls = get_image_urls_from_html(html, img_resolution)
    for url in image_urls:
        download_image(url, IMAGE_FOLDER)


def download_page(url):
    r = requests.get(
        url,
        allow_redirects=False,
        timeout=5,
    )
    if r.status_code != 200:
        print("not corrent status code")
    return r.content.decode("utf-8")


def download_image(url, save_path):
    filename = url.split("/")[-1]
    path = os.path.join(save_path, filename)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print(f"bad status code for {url}")


def get_image_urls_from_html(html, img_resolution):
    html_xml = lxml.html.fromstring(html)
    urls = html_xml.xpath(f'//a[text()="{img_resolution}"]/@href')
    return urls


def create_url(base_url, month_year):
    month, year = month_year[:2], month_year[2:]
    previous_month = str(int(month) - 1).zfill(2)
    previous_month = "12" if previous_month == "00" else previous_month
    month_name = datetime.strptime(month, "%m").strftime("%B").lower()
    new_url = f"{base_url}/{year}/{previous_month}/desktop-wallpaper-calendars-{month_name}-{year}/"  # noqa: E501
    return new_url
