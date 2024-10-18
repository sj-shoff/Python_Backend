from utils.utils_random import random_alfanum


class ShortLinkService:
    def __init__(self):
        self.short_link_to_long_link: dict[str, str] = {}

    def get_link(self, short_link: str) -> str | None:
        return self.short_link_to_long_link.get(short_link)
    
    def put_link(self, long_link: str) -> str:
        short_link = random_alfanum(n=5)

        self.short_link_to_long_link[short_link] = long_link

        return short_link