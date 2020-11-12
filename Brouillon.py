path('<int:pk>/TabooTattoo/', views.DetailView.as_view(), name='detail'),

ça vient de urls.py (mangas)


ça vient de detail.html <li><a href="{% url 'mangas:book' book.id %}">{{ book.book_name }}</a></li>

from book_detail.html <img src="{% static 'mangas/' %}{{book.book_cover_name }}" width="300px" height="400px" alt={{book.book_cover_name}}>