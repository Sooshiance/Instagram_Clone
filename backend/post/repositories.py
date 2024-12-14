from django.db.models import F

from rest_framework.exceptions import ValidationError, PermissionDenied

from .models import (Post,
                     Comment,
                     Album,
                     Like,
                     User
)


class LikeRepository:
    @staticmethod
    def get_like(user:User, post:Post)->bool:
        return Like.objects.filter(user=user, post=post).exists()
    
    @staticmethod
    def create_like_user(user:User, post:Post)->Like:
        if __class__.get_like(user, post):
            raise ValidationError("You have already liked this post.")
        return Like.objects.create(user=user, post=post).save()


class PostRepository:
    @staticmethod
    def create_post(user:User, caption:str, images:list, location:str)->Post:
        post = Post.objects.create(user=user, caption=caption, location=location)
        
        # Prepare a list of Album instances
        album_instances = []
        for image in images:
            if image:
                album_instances.append(Album(post=post, image=image))
            else:
                print("Skipping an invalid image")
        
        if album_instances:
            # Bulk create Album instances
            Album.objects.bulk_create(album_instances)
        else:
            print("No valid images to save in album.")
        
        return post.save()
    
    @staticmethod
    def get_post_by_user(user:User):
        return Post.objects.filter(user=user)
    
    @staticmethod
    def get_post_by_id(post_id:int):
        try:
            return Post.objects.get(pk=post_id)
        except Exception as e:
            raise ValidationError(detail=str(e))
    
    @staticmethod
    def update_post(post_id:int, user:User, caption=None, location=None)->Post:
        try:
            post = Post.objects.get(id=post_id, user=user)
            if post.user != user:
                raise PermissionDenied("")
            if caption:
                post.caption = caption
            if location:
                post.location = location
            post.save()
            return post
        except Exception as e:
            raise ValidationError(detail=str(e))
        
    @staticmethod
    def update_post_likes(post_id:int, user:User)->Post:
        try:
            post = __class__.get_post_by_id(post_id)
            # TODO: We should check user first
            LikeRepository.create_like_user(user, post)
            post.likes = F('likes') + 1
            post.save()
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise ValidationError("Post does not exist.")
        except Exception as e:
            raise ValidationError(detail=str(e))

    @staticmethod
    def delete_post(post_id, user):
        try:
            post = __class__.get_post_by_id(post_id)
            if post.user != user:
                raise PermissionDenied("")
            post.delete()
        except Exception as e:
            raise ValidationError(detail=str(e))


class CommentRepository:
    @staticmethod
    def create_comment(post, user, body):
        return Comment.objects.create(post=post, user=user, body=body).save()

    @staticmethod
    def get_comments_by_post(post):
        return post.comments.all()
    
    @staticmethod
    def get_comment_by_id(comment_id):
        try:
            return Comment.objects.get(pk=comment_id)
        except Exception as e:
            raise ValidationError(str(e))

    @staticmethod
    def update_comment(user, comment_id, body):
        try:
            comment = __class__.get_comment_by_id(comment_id)
            if comment.user != user:
                raise PermissionDenied("")
            comment.body = body
            comment.save()
            return comment
        except Exception as e:
            raise ValidationError(detail=str(e))

    @staticmethod
    def delete_comment(comment_id, user):
        try:
            comment = __class__.get_comment_by_id(comment_id)
            if comment.user != user:
                raise PermissionDenied("")
            comment.delete()
        except Exception as e:
            raise ValidationError(detail=str(e))
