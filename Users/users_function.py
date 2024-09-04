from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from Users.models import Profile, Secions


@sync_to_async
def get_user_profile(user):
    return Profile.objects.get(user=user.id)
@sync_to_async
def get_secions(profile):
    return Secions.objects.get(id=profile.sections.id)
@sync_to_async
def change_profile_user(request, email, quote):
    user = User.objects.get(id=request.user.id)
    user.email = email
    user.save()
    #profile = get_user_profile(user) возвращает асинзронный запрос, пока непонятно как использовать в синхронной функции
    profile = Profile.objects.get(user=user.id)
    profile.quote = quote
    profile.save()
    return 0