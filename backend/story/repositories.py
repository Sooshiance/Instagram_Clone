from django.db import transaction

from rest_framework.exceptions import ValidationError, PermissionDenied

from .models import Story, Reaction


class ReactionRepositories:
    @staticmethod
    def get_reaction(user, story):
        return Reaction.objects.filter(user, story).exists()
    
    @staticmethod
    def create_reaction_user(user, story):
        if __class__.get_reaction(user, story):
            raise ValidationError("")
        return Reaction.objects.create(user=user, story=story).save()


class StoryRepositories:
    @staticmethod
    def create_story(user, content, img, is_archived):
        story = Story(user=user, content=content, img=img, is_archived=is_archived)
        story.save()
        return story

    @staticmethod
    def get_story_by_id(story_id):
        try:
            return Story.objects.get(pk=story_id)
        except Story.DoesNotExist:
            raise ValidationError("Story not found.")

    @staticmethod
    def update_story(story_id, content, img, user):
        story = __class__.get_story_by_id(story_id)
        if story.user != user:
            raise PermissionDenied("You do not have permission to edit this story.")
        story.content = content
        story.img = img
        story.save()
        return story

    @staticmethod
    def update_story_like(story_id, user):
        with transaction.atomic():
            story = __class__.get_story_by_id(story_id)
            if ReactionRepositories.get_reaction(user, story):
                raise ValidationError("User has already liked this story.")
            ReactionRepositories.create_reaction_user(user, story)
            story.likes += 1
            story.save()
        return story

    @staticmethod
    def delete_story(story_id, user):
        story = __class__.get_story_by_id(story_id)
        if story.user != user:
            raise PermissionDenied("You do not have permission to delete this story.")
        story.delete()
