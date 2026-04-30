from django.db import models

# Create your models here.

class Documentry(models.Model):
    title = models.CharField(max_length=200,null=False)
    category = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='img/',null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class Story(models.Model):
    title = models.CharField(max_length=200,null=False)
    category = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='img/',null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class Food(models.Model):
    title = models.CharField(max_length=200,null=False)
    category = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='img/',null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class Travel(models.Model):
    title = models.CharField(max_length=200,null=False)
    category = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='img/',null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=200,null=False)
    category = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='img/',null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    

class comment(models.Model):
    d_relation = models.ForeignKey(Documentry, on_delete=models.CASCADE, null=True, blank=True)
    s_relation = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True)
    f_relation = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    t_relation = models.ForeignKey(Travel, on_delete=models.CASCADE, null=True, blank=True)
    n_relation = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    User_relation = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.content[:20]