from rytr.helpers import get, search_slug


class Tones:
    @staticmethod
    def list():
        return get(url="tones")

    @staticmethod
    def find_by_slug(slug):
        tones = get(url="tones")
        return search_slug(data=tones["data"], slug=slug)
