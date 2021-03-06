from django.db import models
from nomadgram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class TimeStampledModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # This is not variable things
        abstract = True # Make abstarct base class option

@python_2_unicode_compatible
class Image(TimeStampledModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

@python_2_unicode_compatible
class Comment(TimeStampledModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampledModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, null = True, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)