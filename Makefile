
getwallpapers:
	@poetry run getwallpapers

getwallpapers_env:
	echo 'Create container'

getwallpapers_test:
	poetry run pytest tests

lint:
	@poetry run flake8 wallpaper_downloader tests
