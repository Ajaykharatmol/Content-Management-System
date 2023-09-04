# Content-Management-System

please download zip file & follow steps

1. for running project :

    1. Activate Virtaul env
    2. cd to Content_Management_System
    3. pip install django
    4. pip install -r requirements.txt
    5. python manage.py makemigrations
    6. python manage.py migrate
    7. python manage.py runserver

2. for Admin :

    1. python manage.py createsuperuser or use usernane - Ajay password - 123456
    2. http://127.0.0.1:8000/admin/
    3. Admin can view, edit and delete all the contents created by multiple authors

3. for Authors :

    1. http://127.0.0.1:8000/CreateUserRegister  -   Author is able to register using email & password
    2. http://127.0.0.1:8000/LoginUser           -   Author is able to login using email & password or use Email - ajkharatmol@gmail.com, Password - Ajay@2018, Full Name - Ajay Kharatmol, Phone - 09130661138
    3. http://127.0.0.1:8000/Author              -   Author can create, view, edit and delete contents created by  him only       
    4. http://127.0.0.1:8000/Author/<int:pk>     -   Author can create, view, edit and delete contents created by him only
    5. http://127.0.0.1:8000/search?search=task  -   Users should search content by matching terms in title, body, summary and categories
