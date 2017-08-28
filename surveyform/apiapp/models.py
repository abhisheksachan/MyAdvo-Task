from django.db import models

# Create your models here.


class BaseModel(models.Model):  

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract=True 


class QuestionTypes(BaseModel):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)


class Question(BaseModel):
    text = models.TextField()
    q_type = models.ForeignKey('QuestionTypes')


class QuestionOptions(BaseModel):
    question = models.ForeignKey('Question', related_name='q_options')
    text = models.TextField()


class Form(BaseModel):
	name = models.CharField(max_length=255)


class FormQuestions(BaseModel):
	form = models.ForeignKey('Form')
	question = models.ForeignKey('Question')
