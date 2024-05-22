DJANGO TUTORIAL
first open a terminal in VS code or any other text editor 
Create a folder at your desired location
Create a virtual enviroment with (py -m venv .venv)
start the virtual enviroment (source .venv/Scripts/activate) note to deactivate the virtual enviroment use (deactivate)
Install django (py -m pip install Django). If you are asked to update pip use (py -m pip install -U pip)
Create a django project (django-admin startproject myproject) where "myproject" is the project name
Start the server to make sure that it is working. Navigate to the main folder of the project, use (py manage.py runserver)


ADDING URL PATH
Navigate to the urls tab on VS code and locate the url patterns section
add path under the admin path:
        path('',),
        path('about/',),
        path('services/',),

CREATING A VEIW FILE
Create a file in the same folder location as the urls called views.py
import HttpResponse from django.http ( from django.http import HttpResponse)
Create a function for the routed pages
        from django.http import HttpResponse

        def homepage(request):
            return HttpResponse("Hello world: Welcome to home page")

        def about(request):
            return HttpResponse("welcome to about page")

        def services(request):
            return HttpResponse("This is about")

Go back to urls.py file and add the functions that was created in views.py.
    first import views (from . import views)
        urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.homepage),
        path('about/', views.about),
        path('services/', views.services),
        ]
    

CREATING HTML or CSS FILES IN DJANGO
1. Create a new folder called templates in the same project folder as manage.py
2. create each of the HTML files and configure it.

In other for django to recognize the files do the following:
1. go to settings.py file
2. navigate to 'DIRS': Under TEMPLATES which is the directory folder
3. put in templates in the brackets in from of the DIR ('DIRS': ['templates'],)
4. Go to views.py file and import the html files
   1. import render from django.shortcuts( from django.shortcuts import render)
   2. return render from each of the functions created and give a request   and html page parametters: ( 
        def homepage(request):
        # return HttpResponse("Hello world: Welcome to home page")
        return render(request, 'home.html')

        def about(request):
        # return HttpResponse("welcome to about page")
        return render(request, 'about.html')

        def services(request):
        # return HttpResponse("This is services page")
        return render(request, 'services.html') 
        )

CSS AND JS FILE CREATION:

1. create a new folder in the same folder location as templates and name it static
2. inside the folder, create a new folder called css
3. inside the css folder create a new file called style.css
4. Style your css as required
5. Go to settings.py
6. Import os at the top of the page (import os)
7. Scroll towards the down of the page where STATIC_URL is located
8. Create another static file:
   
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
]

9. Go to the home.html template file.
10. Under the <!DOCTYPE html> create the static loader ( {% load static %})
11. link the CSS file: <link rel="stylesheet" href="{% static 'CSS/style.css' %}">
12. for JS do the same but link with script: <script src="{% static 'js/main.js' %}" defer></script>

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

CREATING DJANGO APP(Application)
Apps help you to create reusable components that can be used in other Django projects. It makes creating bigger projects easier to handle.
To create django app
1. Run the following command (py manage.py startapp posts)
2. in views.py that is inside the just created app define a function:
        def post_list(request):
            return render(request, '')

3. In other for django to understand and recognize that we have created a new app go to settings.py and add the app name to installed app section. In this case ('posts') was used.
4. In the post directory, create a folder or directory called template.
5. in the template folder created create a folder called post
6. create a html page (posts_list.html)
7. create html boiler plate


To create urls.py for post directory
1. copy the content of previous url directory
        from django.urls import path
        from . import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.homepage),
            path('about/', views.about),
            path('services/', views.services),
        ]
2. Create a urls.py file inside the post directory and past the content copied. then edit it to show only the home path
            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.posts_list),
            ]
3. Inside the views.py file, add 'posts/posts_list.html' as the second perameter for the post_list created.
            from django.shortcuts import render

                # Create your views here.
                def posts_list(request):
                return render(request, 'posts/posts_list.html')


Go and register the the new urls.py file that was created inside the old urls.py file that we have, to do that, do the following
1. Navigate to the previous url.py file.
2. import include in the path import line.
3. create a posts path for the new urls.py using include path('posts/', include('posts.urls'))



CREATING A SIMPLE LAYOUT NAV BAR TEMPLATE FILES FOR APPLICATION
1. In the template folder, create a html file called layout
2. Import default html boiler plate and include default css load sheet to load the css files.
3. Change document title using block.
             <title>
        {% block title %}
            Django App
        {% endblock title %}
        </title>
4. create two sections in the body section of our page. nav amd main.
5. Create a block content in the main section
6. create the different bar or anchor tags in the nav section corresponding to the pages you have already.
            <!DOCTYPE html>
            {% load static %}
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>
                    {% block title %}
                        Django App
                    {% endblock title %}
                </title>
                <link rel="stylesheet" href="{% static 'css/style.css' %}">
                <script src="{% static 'js/main.js' %}" defer></script>
            </head>
            <body>
                <nav>
                    <a href="/">HOME</a>
                    <a href="/about">ABOUT</a>
                    <a href="/contact">CONTACT</a>
                </nav>
                <main>
                    {% block content %}
                    {% endblock content %}
                </main>
                
            </body>
            </html>

TO USE TEMPLATE
1. In each of the pages. html created eg home.html extend layout.html so that the functions of each of the pages will use the template in the layout section.

                {% extends "layout.html" %}

2. Create blocks for title and content that will replace the default layout block

                {% block title %}
                    About
                {% endblock title %}

                {% block content %}
                    <h1>Home</h1>
                    <h2> This is my Home Page. Welcome </h2>
                    <h1> Check out my <a href="/about">About</a> page.</h1>
                {% endblock content %}

3. DO this for all pages.



PYTHON DJANGO MODELS MIGRATIONS
 Since in the data base, each code will be in a table. The models when created is migrated and turns into table in a data base.

 CREATING A MODEL:
 1. create a class Post models.model

        Class Post(models.model):

 2. Define the model ( this are the Items in the Model)
        title
        body
        slug
        date
 3. Create properties for each of the models created. 
        title = models.CharField(max_length=75)
        body = models.TextField()
        slug = models.SlugField()
        date = models.DateTimeField(auto_now_add=True)
4. Migrate all Django default migrations

        py manage.py migrate

5. Migrate the file created:

        py manage.py makemigrations

6. Apply the files to the data base or lets say send the file to the database.

        py manage.py migrate


PYTHON ORM INTRO TUTORIAL
ORM is Object Relational Mapping. This is the intermidiary between our python code and data base. This means that when model is created it serves as intermidiary betwween the python code and data base. ORM can be accessed via shell. the procedure for working on ORM is:

1. Type py manage.py shell in a terminal.
2. import Post: from posts.models import Post
3. create an instance: p = Post()
4. If you want to check the instance that has been created you type: p and hit enter.
5. To apply an item in the instance lets say title: p.title = "My first Post!"
6. To save the title or item created, use: p.save()
7. To retrive all the objects in the post: Post.objects.all()

In other to tell the differnet post that we have just incase we have more than one post we create a method by doing the following:
1. Go to models.py and create a method which is like a function but part of a class.
   
            def __str__(self):
                return self.title
2. Go back to terminal and navigate to shell then call Post from Posts.models after which you create an instance Post with a title assign an object to title.  