from django.core.exceptions import ValidationError


def get_image_path(instance, file):
    return 'media/accounts/{}.{}'.format(instance.user.username, file.split('.')[-1])

def get_file_path(instance, file):
    return 'file/accounts/{}.{}'.format(instance.user.username, file.split('.')[-1])

def image_size(file):
    if (file.size>2097152):
        return ValidationError("سایز فایل می بایست کمتر از 2مگابایت باشد")


MALE = 'm'
FEMALE = 'f'
OTHER = 'o'

CHOICES_LIST = [(MALE,'مرد'),(FEMALE,'بانو'),(OTHER,'دیگر')]