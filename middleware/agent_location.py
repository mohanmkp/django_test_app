



class User_Track:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            print(f"if IP {ip}")
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(f"elseIP {ip}")

        response = self.get_response(request)
        user_agent = request.META['HTTP_USER_AGENT']
        print(user_agent)

        return response



