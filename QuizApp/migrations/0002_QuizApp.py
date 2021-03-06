# Generated by Django 2.1.1 on 2020-03-20 14:09

from django.db import migrations

def create_data(apps, schema_editor):
    Quiz = apps.get_model('QuizApp', 'Quiz')
    Quiz(question="What year is this?", label="test", order=0, choice1="1999",
     choice2="2999", choice3="2019", choice4="2020", correctAnswer= "2020").save()
    Quiz(question="What month is this?", label="test", order=1, choice1="Janunary",
     choice2="Feburary", choice3="March", choice4="April", correctAnswer= "March").save()
    Quiz(question="What animal can fly?", label="test", order=2, choice1="tiger",
     choice2="bear", choice3="bird", choice4="fish", correctAnswer= "bird").save()
    Quiz(question="What is the sun?", label="test", order=3, choice1="star",
     choice2="nebular", choice3="black hole", choice4="planet", correctAnswer= "star").save()
    Quiz(question="What is 1+1?", label="test", order=4, choice1="1",
     choice2="4", choice3="3", choice4="2", correctAnswer= "2").save() 

class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
