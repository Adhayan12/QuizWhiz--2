from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Feature
from .models import question
from .models import QuizResult                                                        
from django.contrib.auth.models import User,auth
from django.contrib import messages
def index(request):
    #return HttpResponse('<h1>Hello, world</h1>')
    #name = 'abhat'
    #return render(request, 'index.html', {'name': name})
    # feat = Feature(
    #     bod='30th Jan, 2006',
    #     phone=9532428841,
    #     city='Lucknow',
    #     age=19,
    #     degree='Diploma',
    #     email='adhayansri@gmail.com'
    # )
    # return render(request, 'index.html', {'feat': feat})
    return render(request, 'index.html')

def counter(request):
    posts = [1,2,3,4,5,'jim','jey','solo']
    return render(request, 'counter.html', {'posts': posts})
    
#     #text=request.GET['text'] simplest way of getting data
#     text=request.POST['text'] #safe, does not show input data on search box
#     x=len(text.split())
#     return render(request,'counter.html',{'amount':x})
                        
                        
                        
                        
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')  
        password2 = request.POST.get('password2', '')
        
        if not username or not email or not password or not password2:
            messages.error(request, 'All fields are required')
            return redirect('register')
        
        if password==password2:
            if User.objects.filter(email=email).exists(): #to check whether the inputted email already exists in the database or not
                messages.error(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
        
        
   
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # Correct usage
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    return render(request, 'login.html')
                            
                            
def logout(request):
    auth.logout(request)
    return redirect('index')  


def post(request, pk):
    return render(request, 'post.html', {'pk':pk})      


from django.contrib.auth.decorators import login_required
  

def home(request):
    return render(request, 'home.html') 

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from mypro.models import question, QuizResult  # Import the models
import random

def ques(request):
    # Get the selected category from the query parameter
    category = request.GET.get('category')

    if not category:
        # Redirect to home page if no category is selected
        return redirect('home')

    # Save the selected category in the session
    request.session['category'] = category

    # Fetch 30 random questions for the selected category
    questions = list(question.objects.filter(category=category).order_by('?')[:30])  # Select 30 random questions
    total_questions = len(questions)
    maxscore = total_questions * 3

    # Initialize or fetch session data
    if 'current_question' not in request.session:
        request.session['current_question'] = 0
        request.session['score'] = 0
        request.session['answered'] = []
        request.session['random_questions'] = [q.id for q in questions]  # Store random question IDs in the session

    # Fetch random questions stored in the session
    random_questions_ids = request.session.get('random_questions', [])
    questions = question.objects.filter(id__in=random_questions_ids)
    
    current_question_index = request.session['current_question']

    # If all questions are answered
    if current_question_index >= total_questions:
        score = request.session.get('score', 0)

        if request.user.is_authenticated:
            # Save the result for logged-in users
            QuizResult.objects.create(
                user=request.user,
                category=category,  # Save the selected category
                score=score,
                total_score=maxscore
            )
        else:
            print(f"Anonymous user scored {score} out of {maxscore}")

        # Clear the session to reset for a new quiz
       # Remove only quiz-related session data
        quiz_keys = ['current_question', 'score', 'answered', 'random_questions', 'category']
        for key in quiz_keys:
            if key in request.session:
                del request.session[key]


        return render(request, 'result.html', {
            'score': score,
            'total_questions': total_questions,
            'maxscore': maxscore,
            'category': category
        })

    # Get the current question
    current_question = questions[current_question_index]

    if request.method == 'POST':
        selected_answer = request.POST.get('ans')

        # Check if the answer is correct
        if selected_answer == current_question.answer:
            request.session['score'] += 3
        else:
            request.session['score'] = max(0, request.session['score'] - 1)

        request.session['answered'].append(selected_answer)
        request.session['current_question'] += 1

        return redirect(f"{request.path}?category={category}")

    return render(request, 'ques.html', {
        'question': current_question,
        'index': current_question_index + 1,
        'total_questions': total_questions,
        'maxscore': maxscore,
        'category': category
    })

@login_required
def profile(request):
    quiz_history = QuizResult.objects.filter(user=request.user).order_by('-date_taken')  # Get user's quiz history
    return render(request, 'profile.html', {'quiz_history': quiz_history})
   
   
def requestlogin(request):
    return render(request, 'requestlogin.html')   