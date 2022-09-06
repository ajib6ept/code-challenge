
getwallpapers:
	@poetry run getwallpapers

getwallpapers_env:
	echo 'Create container'

getwallpapers_test:
	poetry run pytest tests

lint:
	@poetry run flake8 wallpaper_downloader tests

mypy:
	@poetry run mypy --strict .

test:
	poetry run pytest -vvs --doctest-modules
