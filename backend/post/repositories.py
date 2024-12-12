from django.db.models import F

from rest_framework import exceptions

from .models import (Post,
                     Comment,
                     Album,
)


class PostRepository:
    @staticmethod
    def create_post(user, caption, images, location=None):
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
        
        return post
    
    @staticmethod
    def get_post_by_user(user):
        return Post.objects.filter(user=user)
    
    @staticmethod
    def update_post(post_id, caption=None, location=None):
        post = Post.objects.get(id=post_id)
        if caption:
            post.caption = caption
        if location:
            post.location = location
        post.save()
        return post
    
    @staticmethod
    def get_post_by_id(post_id):
        try:
            return Post.objects.get(pk=post_id)
        except Exception as e:
            raise exceptions.ValidationError(detail=str(e))
        
    @staticmethod
    def update_post_likes(post_id):
        post = Post.objects.filter(pk=post_id).update(likes=F('likes') + 1)
        return Post.objects.get(pk=post_id)

    @staticmethod
    def delete_post(post_id):
        Post.objects.filter(id=post_id).delete()


class CommentRepository:
    @staticmethod
    def create_comment(post, user, body):
        return Comment.objects.create(post=post, user=user, body=body)

    @staticmethod
    def get_comments_by_post(post):
        return post.comments.all()

    @staticmethod
    def update_comment(comment_id, body):
        comment = Comment.objects.get(id=comment_id)
        comment.body = body
        comment.save()
        return comment

    @staticmethod
    def delete_comment(comment_id):
        Comment.objects.filter(id=comment_id).delete()
