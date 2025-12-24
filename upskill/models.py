from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from datetime import date

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


def validation_age(birth_date):
        today = date.today()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        if age < 7:
            raise ValidationError('Age can not be younger than 7')



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(('male','Male'),('female','Female')), null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def display_name(self):
        return self.full_name or self.username




   


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='instructors/', blank=True, null=True)

    expertise = models.CharField(
        max_length=255,
        help_text="Masalan: Python, Frontend, Data Science"
    )

    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name



class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(Teacher,related_name='courses',on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subject,related_name='courses',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    overview = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']

    
    


class Module(models.Model):
    course = models.ForeignKey(Course,related_name='modules',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    overview = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(Module,related_name='contents',on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model__in":(
                'text',
                'video',
                'image',
                'file'
            )
        }
    )
    
    object_id = models.PositiveIntegerField()

    item = GenericForeignKey(
        'content_type',
        'object_id'
    )
    


class ItemBase(models.Model):
    owner = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Text(ItemBase):
    module = models.ForeignKey(Module, related_name='texts', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

class File(ItemBase):
    module = models.ForeignKey(Module, related_name='files', on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='files')

class Video(ItemBase):
    module = models.ForeignKey(Module, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to='videos/', verbose_name="Video File")
    
    def __str__(self):
        return self.title

class Image(ItemBase):
    module = models.ForeignKey(Module, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images')
