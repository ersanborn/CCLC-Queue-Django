from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Question

from .forms import AnswerForm


def index(response):
    template = loader.get_template("question_queue/index.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def student(response):
    template = loader.get_template("question_queue/student/student.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def instructor(request):
    user = "Dr.Professor"
    questions = Question.objects.all()

    # Initialize data to be
    table_data = []

    # Add all query'd data the table that will passed as context
    for question in questions:
        question_info = {
            "id": str(question.id),
            "name": question.asked_by.first_name,
            "class": question.course.name,
            "time": question.created_at,
            "message": question.message,
        }
        table_data.append(question_info)

    context = {
        "question_queue": "",
        "questions": table_data,
        "user": user,
        "form": AnswerForm,
    }

    if request.method == "POST":
        print(request.POST.get("question", "error"))
        print(request.POST.get("replied_by", user))
        print(request.POST.get("message", "error"))
        print(request.POST.get("answer", "off"))
        # This return makes it so we don't get new POSTs on refresh
        return redirect("/instructor/", context)

    return render(request, "question_queue/instructor.html", context)


def coach(response):
    template = loader.get_template("question_queue/coach.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))
