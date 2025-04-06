def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        result = get_response(request, *args, **kwargs)
        return result

    return middleware