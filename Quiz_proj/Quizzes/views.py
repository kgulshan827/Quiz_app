from django.shortcuts import render,redirect
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .forms import Createquiz
# Create your views here.
from django.forms.models import model_to_dict
from Questions.models import Question,Answer
from Answer.models import Result
class QuizListView(ListView):
    model=Quiz
    template_name='main.html'

def quiz_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    return render(request,'quiz.html',{'quiz':quiz})





def quiz_data_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    questions=[]
    for q in quiz.get_questions():
        answer=[]
        for a in q.get_answers():
            answer.append(a.text)
        questions.append({str(q):answer})
    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })
def save_data(request,pk):
    #print(request.POST)
    #return JsonResponse({'text':'works'})
    if(request.is_ajax()):
        data=request.POST
        data_=dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        #print(data_)
        questions=[]
        results=[]
        for k in data_.keys():
            question=Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        user=request.user
        quiz=Quiz.objects.get(pk=pk)
        score=0
        correct_ans=None
        multiplier=100/(len(questions))
        for q in questions:
            answer_selected=request.POST.get(q.text)
            correct_ans=Answer.objects.filter(question=q).get(correct=True)
            print(answer_selected)
            if(answer_selected!=""):
                
                if(answer_selected==correct_ans.text):
                    score=score+1
                results.append({str(q):{'correct_answer':correct_ans.text,'answered':answer_selected}})
            else:
                results.append({str(q):{'correct_answer':correct_ans.text,'answered':'None'}})
                


            
                
        
        score=score*multiplier
        Result.objects.create(score=score,quiz=quiz)
        
        if(score>quiz.required_score):
            return JsonResponse({'Passed':True,'score':score,'results':results})
        else:
            return JsonResponse({'Passed':False,'score':score,'results':results})
    
def result_view(request,pk,score):
    obj=Result.objects.order_by('-pk')[0]
    quiz=Quiz.objects.get(pk=pk)
    return render(request,'result.html',{'obj':obj,'quiz':quiz})


def createquiz(request):
    if request.method == 'POST':
        form=Createquiz(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('Quizzes:main_view')
    else:
      form=Createquiz()
    return render(request,'create_quiz.html',{'form':form})