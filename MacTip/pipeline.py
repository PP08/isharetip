from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile


from MacTip.models import UserProfile
from requests import request, HTTPError

def new_users_handler(backend, user, response, *args, **kwargs):

    if "id" in response:
        try:
            if backend.name == 'facebook':
                url = "http://graph.facebook.com/%s/picture" \
                      % response["id"]
                avatar = request('GET', url, params={'type': 'square', 'height': 1024, 'width': 1024})
                # profile = UserProfile.objects.update_or_create(user=user)
                # profile.profile_photo.save(slugify(user.username + " social") + '.jpg',
                #                            ContentFile(avatar.content))
                profile = UserProfile(user=user)
                # profile.save()
                obj, created = UserProfile.objects.update_or_create(user=user)
                obj.profile_photo.save(slugify(user.username + " social") + '.jpg',
                                           ContentFile(avatar.content))
        except HTTPError:
            pass