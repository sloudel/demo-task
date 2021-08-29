from django.db import models
from django.db.models import F


# абстрактный
class Base(models.Model):
    title = models.CharField(max_length=512)
    
    class Meta:
        abstract = True

class Page(Base):
    def __str__(self):
        return self.title

    def increase_view_counter(self):
        for content in self.content_set.all():
            if content.video:
                content.video.increase_view_counter()
            if content.audio:
                content.audio.increase_view_counter()
            if content.audio:
                content.audio.increase_view_counter()

# абстрактный
class ContentBase(Base):
    view_counter = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title + f', 👁: {self.view_counter}'
    
    def increase_view_counter(self):
        if self:
            self.view_counter = F('view_counter') + 1
            self.save()

class Video(ContentBase):
    data_file = models.FileField(upload_to='static/video/%Y/%m/%d/')
    subtitles_file = models.FileField(upload_to='static/subtitles/%Y/%m/%d/', blank=True, null=True)

class Audio(ContentBase):
    data_file = models.FileField(upload_to='static/audio/%Y/%m/%d/')
    bitrate = models.IntegerField(blank=True, null=True)

class Text(ContentBase):
    data = models.TextField()

class Content(models.Model):
    """
    Вспомогательная модель, создана для того, 
    чтобы контент можно было расставлять в любом порядке
    """
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, null=True, blank=True)
    text = models.ForeignKey(Text, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        name = []
        if self.video:
            name.append(f'video: {self.video}')
        if self.audio:
            name.append(f'audio: {self.audio}')
        if self.text:
            name.append(f'text: {self.text}')
        return ','.join(name)












