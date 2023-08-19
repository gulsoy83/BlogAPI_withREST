# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250, unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_ownedbyuser')
    body = models.TextField()
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    draft = models.BooleanField(default=False)
    
    publish = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts_ownedbymodifieruser', null=True)
    
    image = models.ImageField(upload_to = 'post_api/' , blank=True)
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return "Post<" + str(self.pk) + ">: " + self.title + " | " + self.author.username

    def save(self, *args, **kwargs):
        if self.id: #post daha once yaratilmissa modifiye ediliyordur.
            self.modified = timezone.now()
        if not self.slug: #mevcutta slug varsa ve post update ediliyorsa yeni slug verme.
            self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super(Post,self).delete(*args, **kwargs)
    
    def get_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique = slug
        number = 1
        while Post.objects.filter(slug = unique).exists():
            unique = '{}-{}'.format(slug,number)
            number += 1
        return unique

class Comment(models.Model):
    publish = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments_ownedbymodifieruser', null=True)
    
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_ownedbyuser')
    masterPost = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments_linkedtothispost')
    
    #bir yorum, baska bir yorumun altina atildiysa;
    masterComment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comments_linkedtomasterComment')
    
    #bir yoruma bagli diger yorumlari listele.
    def children(self):
        return Comment.objects.filter(masterComment = self)
    
    #adding the @property decorator to that method would allow you to access its computed value like a model attribute without parenthesis. a.checkChildren vs a.checkChildren()
    @property
    def checkChildren(self):
        return Comment.objects.filter(masterComment = self).exists

    class Meta:
        ordering = ('-modified',)

    def save(self, *args, **kwargs):
        if self.id:
            self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


    def __str__(self):
        return "Comment<" + str(self.pk) + ">: " + "  {" +  str(self.masterPost.slug) + "}   [" + self.author.username + "]"