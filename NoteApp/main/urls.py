from django.urls import path
from . import views


urlpatterns=[

	path('register/',views.register_view,name='register'),
	path('login/',views.Login_view.as_view(),name='login'),
	path('logout/',views.logout_view,name='logout'),
	path('notes/',views.notes,name='notes'),
	path('create-note/',views.create_note,name='create-note'),
	path('note/<int:pk>',views.note_detail,name='note-detail'),
	path('note-delete/<int:pk>',views.note_delete,name='note-delete')
	
]