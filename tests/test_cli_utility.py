import subprocess
from typing import List, Tuple

import pytest
from click.testing import CliRunner
from pytest_mock import MockFixture

from wallpaper_downloader.cli import arg_parse
from wallpaper_downloader.downloader import create_url

FAIL_PARAMETRS = (
    ["640x480"],
    ["640x480", "072017"],
    ["072017", "640x4801"],
    ["1072017", "640x480"],
    ["072000", "640x480"],
    ["072100", "640x480"],
    ["072017", "800x720"],
)

GOOD_PARAMETRS = (["092017", "640x480"], ["092018", "1366x768"])

CORRECT_URLS = (
    [
        "072017",
        "https://www.smashingmagazine.com/2017/06/desktop-wallpaper-calendars-july-2017/",  # noqa: E501
    ],
    [
        "012022",
        "https://www.smashingmagazine.com/2021/12/desktop-wallpaper-calendars-january-2022/",  # noqa: E501
    ],
)


def capture(command: List[str]) -> Tuple[bytes, bytes, int]:
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


@pytest.mark.parametrize("parametrs", FAIL_PARAMETRS)
def test_fail_parametrs_with_subprocess(parametrs: List[str]) -> None:
    command = ["poetry", "run", "getwallpapers"]
    command.extend(parametrs)
    out, err, exitcode = capture(command)
    assert "BadParameter" in err.decode("utf-8")
    assert 0 != exitcode


@pytest.mark.parametrize("parametrs", FAIL_PARAMETRS)
def test_fail_parametrs(parametrs: List[str]) -> None:
    runner = CliRunner()
    result = runner.invoke(arg_parse, parametrs)
    assert result.exit_code != 0


@pytest.mark.parametrize("parametrs", GOOD_PARAMETRS)
def test_good_parametrs(parametrs: List[str], mocker: MockFixture) -> None:
    mocker.patch(
        "wallpaper_downloader.downloader.download_page", lambda x: "0"
    )
    runner = CliRunner()
    result = runner.invoke(arg_parse, parametrs)
    assert result.exit_code == 0


@pytest.mark.parametrize("parametrs", CORRECT_URLS)
def test_correct_create_url(parametrs: List[str]) -> None:
    month_year, correct_url = parametrs
    assert create_url(month_year) == correct_url
