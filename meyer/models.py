from django.db import models
#from tinymce.models import HTMLField
#from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
#from froala_editor.fields import FroalaField
from froala_editor import fields

# Create your models here.
class Topic(models.Model):
    order = models.IntegerField()
    title = models.TextField(blank=True)
    css_class = models.CharField(max_length=250, blank=True)
    background_img = models.ImageField(upload_to="background", blank=True)
#    content = tinymce_models.HTMLField()
    content = models.TextField(blank=True)
    mobile_content = models.TextField(blank=True)
    icon = models.CharField(max_length=250, blank=True)
#    content = models.TextField(blank=True)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return "Topic: "+self.title

    def url(self):
        return self.title.replace(' ','_')


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="subtopics")
    order = models.IntegerField()
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
#    content = tinymce_models.HTMLField()
#    content = fields.FroalaField(options={
#        'image_upload':True
#  })
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.topic.title+" | "+self.title

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to="backgrounds");
    css_class = models.CharField(max_length=250, blank=True)
