from django.shortcuts import render,redirect,get_object_or_404
from . models import Note
from django.contrib.auth import login , logout
from .forms import NoteForm,RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


def notes(request):
	notes = Note.objects.all().filter(user = request.user)
	return render(request,'main/notes.html',{'notes':notes})


def register_view(request):
	if request.method =='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request,'main/register.html',{'form':form})


class Login_view(LoginView):
	template_name = 'main/login.html'
	fields = '__all__'
	redirect_authenticated_user = True
	def get_success_url(self):
		return reverse_lazy('notes')




def logout_view(request):
	logout(request)
	return redirect('login')


def create_note(request):

	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user 
			note.save()
			return redirect('notes')
	else :
		form = NoteForm()
	return render(request,'main/create_note.html',{'form':form})



def note_detail(request,pk):
	note = get_object_or_404(Note,pk=pk)

	form = NoteForm(instance = note)

	if request.method =='POST':
		form = NoteForm(request.POST,instance = note)
		if form.is_valid():
			form.save()
			return redirect('notes')

	return render(request,'main/note_detail.html',{'form':form})

	
def note_delete(request,pk):
	note = get_object_or_404(Note,pk=pk)
	Note.objects.filter(pk = pk).delete()
	return redirect('notes')