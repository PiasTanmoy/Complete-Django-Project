# CompleteDjangoProject
An ecomerece website for learning and teaching purposes

<img src="media/slider/nature3.jpg">

Django Project Guide
A cheat sheet provided by your course teacher :D 






Make the path from Django to Browser 




Create an ER diagram
Find the entities or classes of the project
Analyse the relationship between the entities 
Use a professional tool to create the ERD
Add necessary attributes to every entity 
Note: ER diagram might change during the development process

Create Schema diagram
Use the standard rules to derive the schema diagram from ERD









Create Project and Upload to GitHub
One member should create a new project (without any virtual environment)
Share the project with your team member and me. 
Create and Upload a Django Project to GitHub 


Create APPs



Divide the project into different apps based on the functionality. There is no right or wrong design here. But there are good and bad designs. Good design will help you to manage the project efficiently.

For example: If you want to develop an university management system, you might create the following apps 
StudentManagement
FacultyManagment
CourseManagement
StaffManagement
Administration
ClubManagement 
Accounts
EventManagement 
Department 
and so on 


Implement models 
Every app has its own models.py
Implement models according to the schema diagram (within the appropriate app)
Import tables from other models if necessary
Use foreign key attribute to create the relationships among the tables 
Add “on delete” attribute to the foreign key function
Determine the dependencies 
For example: consider the following tables
	
Person is independent as it is not pointing to another table. On the other hand, Address table is pointing to the Person table (with a foreign key personid) 
StudentManagement/models.py 


CourseManagement/models.py


Create forms 
Initially forms.py is not created inside an app. So, inside the app directory create a new form.py 
Import model Class from models.py
Create a new class for form and inherit with ModelForm
Create a class Meta 
Inside the Meta, add mode and fields
fields == ‘__all__’ means all fields of the model

Example: 

Note: you don’t need to create forms for next week’s update.
Create views 
Show database table in HTML page
Import the model Class
Define a function and search the table for all objects
Add the resulting query set in the context
Pass the context in the render function
Also add the request and html page in the render function 
StudentManagement/views.py


Take input to database table from HTML page
Create anHTML page to take input. Just use form in the HTML page 

Create a views function to upload books

Create an url for this function



Create HTML pages 
Create directories with the APPs name
To show database table
Inside the template/app add a HTML page (example: showStudents.html) 
Use a for loop to iterate through the query set  
Print the information using {{ }} 
To insert the data into database table 
Will be added later. Stay tuned!

templates/StudentManagement/studentlist.html

When someone asks how is CSE 309 & 310 going ?




User Registration (Sign up)
Create a UserManagement App 
Create an HTML page for user registration

Write codes in views.py


Create an url path and done!
path('signup/', user_views.register, name='register'),





Login
For authentication we will use the build in modules. Write this path in the urls.py

path('accounts/', include('django.contrib.auth.urls')),

	
Ref: https://docs.djangoproject.com/en/3.1/topics/auth/default/ 


Create a “registration” directory in “templates” and add a “login.html” page.

You need to set Login route by adding a this line in the setting.py
LOGIN_REDIRECT_URL = 'your_url'


Now you can access the login page by using this url after the home url in browser 
/accounts/login/








Logout
Just add LOGOUT_REDIRECT_URL = 'your-url' in settings.py



Now you can access the logout function by using this url after the home url in browser 
/accounts/logout/

Done!


Change Password
In “templates/registration” directory add a “password_change_form.htm” page


In “templates/registration” directory add a “password_change_done.html” page


Now you can access the password function by using this url after the home url in browser 
/accounts/password_change/



