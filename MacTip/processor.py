from django.contrib.auth.decorators import login_required

from MacTip.models import Category
from social_django.models import UserSocialAuth

def base_info(request):
    categories = Category.objects.all()
    categories_amount = categories.count()
    base_info = {"categories": categories, "categories_amount": categories_amount}
    return base_info


def user_settings(request):
    user = request.user
    # print(user)

    if user.is_anonymous():
        return ({
            'facebook_login': None,
            'groupname': 'Anonymous',
        })
    else:
        try:
            groupname = user.groups.all().first().name
            facebook_login = user.social_auth.get(provider='facebook')
            # print(user.groups.all().first().name)
        except UserSocialAuth.DoesNotExist or AttributeError:
            facebook_login = None
            groupname = "Anonymous"
        # can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
        return ({
            'facebook_login': facebook_login,
            'groupname': groupname,
        })
