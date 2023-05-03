from pages.yadisk import YandexDisk

yandex_disk = YandexDisk()

def test_create_folder():
    yandex_disk.create_folder()
    yandex_disk.get_folder()
    yandex_disk.delete_folder()
    yandex_disk.get_deleted_folder()
