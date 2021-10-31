from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from .models import Question
from .serializer import QuestionSerializer
# import json

@api_view(['GET', 'POST'])
def Question_list(request):
    """
    List all Questions, or create a new Question.
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        try:
            serializer = QuestionSerializer(data=question_data)
            if serializer.is_valid():
                print('reached here')
                serializer.save()
                return JsonResponse({"status": "201 question added", "id": len(Question.objects.all())})
        except:
            return JsonResponse({"status": "404 bad request"}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Question_lookup(request, id):
    try:
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)    
    except:
        return JsonResponse({"status": "404 Not Found", "Reason": f"Question with id = {id} not found"})