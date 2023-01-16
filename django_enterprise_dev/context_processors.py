def global_context(request):
    return {
        'base_url': request.build_absolute_uri(
            '/'
        )[:-1].strip('/'),
    }

# remove the last slash in base url -- [:-1].strip('/'),
