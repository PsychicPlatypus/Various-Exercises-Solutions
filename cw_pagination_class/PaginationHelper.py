# TODO: complete this class
import math


class PaginationHelper:
    def __init__(self, collection: list[str], items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page
        pages = dict()
        page = 0
        items = len(collection)
        while items > 0:
            if items > items_per_page:
                pages.update({page: items_per_page})
                items -= items_per_page
                page += 1
            else:
                pages.update({page: items})
                items = 0

        self.pages = pages

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index: int):
        if page_index not in self.pages.keys():
            return -1
        return self.pages.get(page_index)

    def page_index(self, item_index):
        if item_index > len(self.collection) - 1 or item_index < 0:
            return -1
        return item_index // self.items_per_page
