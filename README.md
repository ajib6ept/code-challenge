### Задача 2: Smashing Wallpaper Downloader 

[Ссылка](https://github.com/ostrovok-team/code-challenge/tree/master/python)

Есть прекрасный сайт Smashing Magazine, который каждый месяц выкладывает отличные обои для десктопа. Заходить каждый месяц и проверять, что там нового дело не благородное, поэтому давайте попробуем автоматизировать эту задачу.
Требуется написать cli утилиту, которая будет качать все обои в требуемом разрешение за указанный месяц-год в текущую директорию пользователя. Вот [тут](https://www.smashingmagazine.com/tag/wallpapers/) находятся все обои, а [здесь](https://www.smashingmagazine.com/2017/04/desktop-wallpaper-calendars-may-2017/) находятся обои за май 2017.

Условия:
* Python 3.5+
* Любые сторонние библиотеки
* PEP8
* Если останется время, то можете покрыть её тестами с помощью py.test (:

Подготовить среду, установить зависимости(откроет консоль внутри контейнера)
```
make getwallpapers_env
```
Запустить скрипт загрузки обоев в консоли из предыдущей команды:
```
./getwallpapers.py 022018 640x480
```
Запустить тесты
```
make getwallpapers_test
```
Особенности:
* Если обои доступны в вариантах с календарём и без, утилита скачает оба.
* Не все обои доступны во всех разрешениях, если конкретных обоев запрошенного разрешения нет, утилита их пропустит.
