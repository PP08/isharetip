from django.contrib.auth.decorators import login_required

from MacTip.models import Category, UserProfile
from social_django.models import UserSocialAuth
from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.database
tb = db.category

def base_info(request):
    post_categories = Category.objects.all()
    post_categories_amount = post_categories.count()
    app_categories = list(tb.find())
    app_categories = [x["name"] for x in app_categories]
    app_categories = sum(app_categories, [])
    app_categories = list(set(app_categories))
    app_categories_amount = len(app_categories)
    base_info = {"post_categories": post_categories, "post_categories_amount": post_categories_amount,
                 "app_categories": app_categories, "app_categories_amount": app_categories_amount,}
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
            groupname = user.groups.all().first()
            if groupname is not None:
                groupname = groupname.name
            else:
                groupname = 'Anonymous'
            facebook_login = user.social_auth.get(provider='facebook')
            user_avatar = UserProfile.objects.filter(user=user).first().profile_photo.url
            # print(user.groups.all().first().name)
        except UserSocialAuth.DoesNotExist or AttributeError:
            facebook_login = None
            groupname = "Anonymous"
            user_avatar = ''
        # can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
        return ({
            'facebook_login': facebook_login,
            'groupname': groupname,
            'user_avatar': user_avatar,
        })
