from re import U
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manage for user profiles"""
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and use new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve full name"""
        return self.name

    def get_short_name(self):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        return self.email+"::::"+self.name



class UserPostsManager(BaseUserManager):
    """Manage for user profiles"""
    def create_post(self, title, url):
        if not title:
            raise ValueError("Posts must have title")
        
        title = title.set_title(title)
        url = url.set_title(url)
        post = self.model(title=title, url=url)

        post.save(using = self._db)

        return post


class UserPosts(AbstractBaseUser, PermissionsMixin):
    """Database models for user posts"""
    title = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

    objects = UserPostsManager()
    
    REQUIRED_FIELDS = ['title', 'url']


    def get_post_name(self):
        """Retrieve post name"""
        return self.title

    def get_url(self):
        """Retrieve post url"""
        return self.url

    def __str__(self):
        return self.title+"::::"+self.url



class CityManager():
    """Manage for  city"""
    def create_city(self, name, url):
        if not name:
            raise ValueError("Posts must have name")
        name = name.set_name(name)
        city = self.model(name=name)
        city.save(using = self._db)
        return city


class Cities(AbstractBaseUser, PermissionsMixin):
    """Database models for cities"""
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

    objects = CityManager()
    
    REQUIRED_FIELDS = ['name']


    def get_city(self):
        """Retrieve city"""
        return self.name


    def __str__(self):
        return self.name
    
    
 
class FriendRequestManager():
    """Manage for  Friend requests"""
    def create_request(self, from, to):
        if not name:
            raise ValueError("Requests must have from & to ")
        from = from.set_name(from)
        to = to.set_name(to)
        request = self.model(from=from, to=to)
        request.save(using = self._db)
        return request


class FriendRequests(AbstractBaseUser, PermissionsMixin):
    """Database models for friend requests"""
    from = models.CharField(max_length = 255)
    to = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

    objects = FriendRequestManager()
    
    REQUIRED_FIELDS = ['from', 'to']


    def get_requests(self):
        """Retrieve requests"""
        return self.name


    def __str__(self):
        return self.name

    
    
class HashtagManager():
    """Manage for  hash tag"""
    def create_hashtag(self, name, url):
        if not name:
            raise ValueError("Posts must have name")
        name = name.set_name(name)
        hashtag = self.model(name=name)
        hashtag.save(using = self._db)
        return hashtag


class HashTags(AbstractBaseUser, PermissionsMixin):
    """Database models for hash tags"""
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

    objects = HashtagManager()
    
    REQUIRED_FIELDS = ['name']


    def get_hash_tag(self):
        """Retrieve hash tag"""
        return self.name


    def __str__(self):
        return self.name




class OrderManager():
    """Manage for  orders"""
    def create_order(self, items, url):
        if not items:
            raise ValueError("Orders must have items")
        items = items.set_items(items)
        order = self.model(name=items)
        order.save(using = self._db)
        return order


class Orders(AbstractBaseUser, PermissionsMixin):
    """Database models for orders"""
    items = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

    objects = OrderManager()
    
    REQUIRED_FIELDS = ['items']


    def get_orders(self):
        """Retrieve orders"""
        return self.items


    def __str__(self):
        return self.items
