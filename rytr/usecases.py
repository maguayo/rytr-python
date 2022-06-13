from rytr.helpers import get, search_slug


class UseCases:
    @staticmethod
    def list():
        return get(url="use-cases")

    @staticmethod
    def find_by_slug(slug):
        usecases = get(url="use-cases")
        return search_slug(data=usecases["data"], slug=slug)

    @staticmethod
    def get(id):
        return get(url=f"use-cases/{id}")
