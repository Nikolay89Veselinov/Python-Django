def get_username(request, credentials):
    username = credentials.get('username')
    namespace = credentials.get('namespace')
    return namespace, username