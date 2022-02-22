from django.http import JsonResponse

# FUNCTION THAT GET ALL ROUTES 

def getRoutes(request):
    # DEFINING API ROUTES 
    routes =[
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body':None,
            'description':'return a array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body':None,
            'description':'return a single note object'
        },{
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body':{'body':''},
            'description':'Creates new note with data sent in post required body'
        },{
            'Endpoint': '/notes/id/update',
            'method': 'PUT',
            'body':{'body':''},
            'description':'Creates an existing note with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        },
    ]
    return JsonResponse(routes, safe=False)