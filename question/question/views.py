from rest_framework import generics
from .serializers import QuestionSerializer
from .models import Question

class QuestionAPIView(generics.ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializerQe