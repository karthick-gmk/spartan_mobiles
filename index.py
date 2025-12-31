from myapp.wsgi import application

# Vercel serverless function
def handler(request):
    return application(request.environ, request.start_response)