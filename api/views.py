from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note


# FUNCTION THAT GET ALL ROUTES
@api_view(['GET'])
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
    return Response(routes)

# FUNCTION THAT GET ALL NOTES
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# FUNCTION THAT GETS A SINGLE NOTE
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# FUNCTION THAT CREATES A NEW NOTE
@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body=data['body']        
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# FUNCTION THAT UPDATES AN EXISTING NOTE
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# FUNCTION THAT DELETES AN EXISTING NOTE
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note deleted successfully')
