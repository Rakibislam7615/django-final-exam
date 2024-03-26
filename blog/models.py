from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title =models.CharField(max_length = 100)
    sub_title = models.CharField(max_length = 100,default = '')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
   #def first_line(self):
        #return self.content.splitlines()[0] if self.content else ""