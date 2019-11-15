from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
import pytz

# Django Rest Framework for seeing the JSON
# @api_view(['POST'])
# def add_comment(request):
#   # Make a serializer with the JSON from the request
#   serializer = CommentSerializer(data=request.data)
#   # Checks that the JSON has the right fields
#   if serializer.is_valid():
#     # Saves the object to the database
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Display the comments
def blog_post(request):
  if request.POST:
    # Make a serializer with the JSON from the request
    serializer = CommentSerializer(data=request.POST)
    # Checks that the JSON has the right fields
    if serializer.is_valid():
      # Saves the object to the database
      serializer.save()

  # Get all the comments
  db_comments = Comment.objects.all()
  comments = []
  # Just send the day of the comment, not the time
  for comment in db_comments.reverse():
      comments.append({
        'name': comment.name,
        'comment': comment.comment,
        'created': comment.created.date()
      })
      
  # Render the html for the post
  return render(request, 
                template_name="index.html", 
                context={'comments': comments, 'num_comments': len(comments)})