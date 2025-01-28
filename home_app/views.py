<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .utils import send_whatsapp_message 
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            send_whatsapp_message(user.phone_number, "You have successfully registered! Welcome!")

            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been successfully logged in!')

            send_whatsapp_message(user.phone_number, "You have successfully logged into your dashboard!")

            return redirect('dashboard') 
            
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')










@login_required
def dashboard(request):
    if request.method == 'POST':
        # Use the logged-in user's phone number
        recipient_number = request.user.phone_number  # Adjust this to match your User/CustomUser model structure
        message_body = request.POST.get('message_body')  # Get the message body from the form

        if recipient_number and message_body:
            try:
                send_whatsapp_message(recipient_number, message_body)  # Send the WhatsApp message
                messages.success(request, 'Message sent successfully via WhatsApp!')
            except Exception as e:
                messages.error(request, f'Failed to send the message: {str(e)}')
        else:
            messages.error(request, 'Message body cannot be empty!')

    return render(request, 'dashboard.html')



from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def user_logout(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')  # Redirect to login page


=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 47943c7aebd196923dca4de5fb234ee7a12f87eb
