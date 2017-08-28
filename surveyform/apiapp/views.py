from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from models import Form, FormQuestions, Question, QuestionOptions, QuestionTypes
from datetime import datetime

class LoginForm(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        return render(request, "apiapp/index.html")



class LogoutForm(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        return render(request, "apiapp/index.html")


class AccountProfile(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
    	print request.data
        return Response(request.data)


class CreateForm(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        return render(request, "apiapp/create_form.html")


    def post(self, request, *args, **kwargs):

        print request.data
        form_name = request.data.get("form_name", "")
        questions_list = request.data.get("question_lists", "")
        current_date = datetime.utcnow()

        form_obj = Form.objects.create(name=form_name, created_at=current_date, updated_at=current_date)

        for q in questions_list:
            options = q["option_list"]
            ques_text = q["question_text"]
            ques_type = q["question_type"]

            ques_type_obj = QuestionTypes.objects.get(slug=ques_type)
            ques_obj = Question.objects.create(text = ques_text, q_type=ques_type_obj, created_at=current_date, updated_at=current_date)

            if ques_type == "bool":
                print "inside bool"
                QuestionOptions.objects.create(question=ques_obj, text="True", created_at=current_date, updated_at=current_date)
                QuestionOptions.objects.create(question=ques_obj, text="False", created_at=current_date, updated_at=current_date) 
            else:
                for option in options:
                    QuestionOptions.objects.create(question=ques_obj, text=option, created_at=current_date, updated_at=current_date)

            FormQuestions.objects.create(form=form_obj, question=ques_obj, created_at=current_date, updated_at=current_date)

        return Response()



class DisplayForm(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, formid, *args, **kwargs):

        question_list = FormQuestions.objects.filter(form=formid).values('question__text', 'question__q_type__slug', 'question_id', 'form__name')

        for ques in question_list:
            ques["options"] = QuestionOptions.objects.filter(question_id=ques['question_id']).values_list('text', flat=True)
        return render(request, "apiapp/display_form.html", {"question_list": question_list, "form_name": question_list[0]["form__name"]})
