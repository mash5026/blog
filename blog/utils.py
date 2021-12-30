from django.core.exceptions import ValidationError


def get_image_path(instance,file):
    return 'media/post/{}.{}'.format(instance.title,file.split(".")[-1])

def image_size(file):
    if(file.size>2097152):
        return ValidationError("سایز فایل می بایست کمتر از 2مگابایت باشد")


ACCEPT = 0
PENDING = 1
REJECT = 2

CHOICES_LIST_COMMENT = [
    (ACCEPT,'تایید'),
    (PENDING,'در حال بررسی'),
    (REJECT,'مردود')
    ]



