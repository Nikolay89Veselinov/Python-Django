from django.http import HttpResponse


def group_required(groups=[]):
    groups_set = set(groups)
    def decorator(view_func):
        def wrapper(request, *arrg, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *arrg, **kwargs)
            row_groups = request.user.groups.all()
            user_groups = set([group.name for group in row_groups])
            if user_groups.intersection(groups_set):
                return view_func(request, *arrg, **kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper
    return decorator