from django.db import models
import random
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    # author : 인증 뒤에 언급을 해드리도록 하겠습니다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    contents = models.TextField()
    r = random.randint(1, 10000)
    img = models.ImageField(upload_to=f'bb/%Y/%m/%d/{r}', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f'title:{self.title}, contents:{self.contents}'