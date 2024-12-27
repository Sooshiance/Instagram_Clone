from .models import Explorer
from .tasks import reset_clock

from post.models import Post


class ExplorerRepositories:
    @staticmethod
    def all_post_in_first_day(post: Post):
        pass

    @staticmethod
    def all_post_in_all_day(post: Post):
        pass

    @staticmethod
    def comparison_result():
        pass
