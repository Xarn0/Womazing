from main.models import Basket



def basket_count(request):
    count = Basket.objects.filter( user_id_id = request.user.id).count()
    return {'basket_count' : count}
