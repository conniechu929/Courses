from django.shortcuts import render, redirect
from . models import Courses, Descriptions

# Create your views here.
def index(request):
	context = {
		'courses': Courses.objects.all(),
		'descriptions': Descriptions.objects.all()
	}
	return render(request, 'course/index.html', context)

def getCourse(request):
	Courses.objects.create(name=request.POST['name'])
	current_course = Courses.objects.order_by('-id')[0]
	course = Courses.objects.get(id=current_course.id)
	Descriptions.objects.create(description=request.POST['description'], course_id=course)
	return redirect('/', )

def destroy(request, id):
	if request.method == 'POST':
		request.session['id'] = id
		request.session['name'] = Courses.objects.get(id=request.session['id']).name
		request.session['description'] = Descriptions.objects.get(course_id=request.session['id']).description
	return render(request, 'course/destroy.html')

def delete(request):
	Descriptions.objects.get(course_id=request.session['id']).delete()
	Courses.objects.get(id=request.session['id']).delete()
	request.session.clear()
	return redirect('/')