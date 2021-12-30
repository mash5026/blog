from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile,Log

#<<<>>>>>>create profile after create user automaticly<<<>>>>>>
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

#<<<>>>>>>create log after delete profile automaticly that who delete profile<<<>>>>>>
@receiver(post_delete, sender=Profile)
def delete_profile_user(sender, instance, **kwargs):
    import inspect
    for f in inspect.stack():
        if f[3]=='get_response':
            request = f[0].f_locals['request']
            break
        else:
            request = None
    log = Log()
    log.description =  "profile {} ba user {} deleted by {} with {} id".format(instance.id, instance.user.username, request.user, request.user.id)
    log.save()
    instance.user.delete()


#<<<>>>>>>update user after create profile automaticly<<<>>>>>>
@receiver(post_save, sender=Profile)
def update_profile_user(sender,instance, **kwargs):
    instance.user.save()