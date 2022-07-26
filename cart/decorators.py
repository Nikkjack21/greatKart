from functools import wraps
from django.http import request
from django.shortcuts import redirect



def authenticated_user(view_func) :
    pass
    # def wrapper_func(request):

    #     if request.user.is_authenticated:
    #         return view_func(request)

    #     else : 
    #         return redirect('signin')

    # return wrapper_func


def user_log(url):
    @wraps(url)
    def wrapper(request):
        
        if request.user.is_authenticated:
            return url(request)
        else:
            return redirect('signin')
    return wrapper