from account.models import CustomerUser
from restaurant.models import Restaurant

def user_role(request):
    user = None
    role = None

    if request.session.get('user_id'):
        try:
            user = CustomerUser.objects.get(id=request.session['user_id'])
            role = 'customer'
        except CustomerUser.DoesNotExist:
            pass
    elif request.session.get('restaurant_id'):
        try:
            user = Restaurant.objects.get(id=request.session['restaurant_id'])
            role = 'restaurant'
        except Restaurant.DoesNotExist:
            pass

    return {
        'logged_user': user,
        'logged_role': role,
    }
