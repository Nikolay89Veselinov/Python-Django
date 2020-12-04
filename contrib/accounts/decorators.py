from django.shortcuts import redirect


def user_required(ModelClass):
    def decorators(view_func):
        def wrapper(request, id, *args, **kwargs):
            model_obj = ModelClass.objects.get(pk=id)
            if model_obj.user_id == request.user.id:
                return view_func(request, id, *args, **kwargs)
            return redirect('accounts:login')
        return wrapper
    return decorators
