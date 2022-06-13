from rytr.helpers import get, search_slug


class Languages:
    @staticmethod
    def list():
        return get(url="languages")

    @staticmethod
    def find_by_slug(slug):
        languages = get(url="languages")
        return search_slug(data=languages["data"], slug=slug)
