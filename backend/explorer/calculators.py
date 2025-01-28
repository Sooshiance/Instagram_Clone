from post.models import Post


def top_post_formula(post: Post) -> float:
    result = (post.likes / post.views) * 100
    return result
