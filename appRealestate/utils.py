
import random
from django.utils.text import slugify
def slugify_instance_company(instance,save=False,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.property_title)
    Klass = instance.__class__
    qs = Klass.objects.filter(property_slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000,500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_company(instance,save=save,new_slug=slug)
    instance.property_slug  = slug
    if save:
        instance.save()
    return instance
def path_file_name(instance, filename):
    return '/'.join(filter(None, (str(random.randint(300_000,500_000)), filename)))
def img_file_name(instance, filename):
    return '/'.join(filter(None,(str(random.randint(300_000,500_000)), str(instance.id), filename)))
