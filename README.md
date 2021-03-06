## BUILDING JOBPORTAL APP USING DJANGO


### ---------
### 1. SETUP
### ---------

#### 1.1 Create django project, apps, database, templates, static and media files


### ---------------------
### 2. CUSTOM USER MODEL 
### ---------------------


#### 2.1 Create Custom User model Part 1 -  Create MyUserManager, MyUser model and migrations

        modified:   README.md
        new file:   apps/accounts/migrations/0001_initial.py
        modified:   apps/accounts/models.py
        modified:   config/settings.py


#### 2.2 Cusomizing MyUser model, tegister MyUser model to admin and customizing admin display

        modified:   README.md
        modified:   apps/accounts/admin.py


### ---------------------
### 3. CUSTOM USER MODEL 
### ---------------------


#### 3.1 Create a new app 'apps/job' and register it to project


#### 3.2 Create Job model

        modified:   README.md
        modified:   apps/job/admin.py
        modified:   apps/job/models.py


### --------------------
### 4. DISPLAYING JOBS
### --------------------


#### 4.1 Add, retrieve and display jobs on home page

        modified:   README.md
        modified:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   templates/main/index.html


#### 4.2 Filtering jobs list by draft and pubished

        modified:   README.md
        modified:   apps/main/views.py 


#### 4.3 Pagination

        modified:   README.md
        modified:   apps/main/views.py
        new file:   templates/main/inc/recent_jobs.html
        new file:   templates/main/inc/recent_jobs_header.html
        new file:   templates/main/inc/recent_jobs_pagination.html
        modified:   templates/main/index.html


### -------------
### 5. CATEGORY
### -------------


#### 5.1 Create Category model and add OneToMany relationship with Job model

        modified:   README.md
        modified:   apps/job/admin.py
        modified:   apps/job/models.py


#### 5.2 Retrieve and display categories data in home page

        modified:   README.md
        modified:   apps/main/views.py
        modified:   templates/main/index.html


#### 5.3 Retrieving number of jobs in each category and display them in home page

        modified:   README.md
        modified:   apps/main/views.py
        modified:   templates/main/inc/recent_jobs.html
        modified:   templates/main/index.html

        NOTE:

        Recent jobs dis-appear from the home page


#### 5.4 Fixing  problem in 5.3       

        modified:   README.md
        modified:   apps/job/models.py
        modified:   apps/main/views.py
        modified:   templates/main/inc/recent_jobs.html
        modified:   templates/main/index.html


### -----------------------------
### 6. USERS REGISTRATIONS FORM
### -----------------------------


#### 6.1 User register form part 1 - Urls-Views-Templates-Forms

        modified:   README.md
        new file:   apps/accounts/forms.py
        modified:   apps/accounts/urls.py
        modified:   apps/accounts/views.py
        new file:   templates/accounts/user_register.html

#### 6.2 User register form part 2 - Adding fields to UserRegisterForm class

        modified:   README.md
        modified:   apps/accounts/forms.py
        modified:   apps/accounts/views.py


#### 6.3 User register form part 3 - Adding html template user_register.html

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.4 User register form part 4 - Looping the form field  

        modified:   README.md
        modified:   templates/accounts/user_register.html



#### 6.5 User register form part 5 - Showing the form's label

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.6 User register form part 6 - Making the input types

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.7 User register form part 7 - Showing the placeholders

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.8 User register form part 8 - Adding form method

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.9 User register form part 9 - Limiting the form fields to 5

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.10 User register form part 10 - Adding input user type

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.11 User register form part 12 - Adding csrf_token for security reason

        modified:   README.md
        modified:   templates/accounts/user_register.html


#### 6.12 User register form part 12 - Adding form button

        modified:   README.md
        modified:   templates/accounts/user_register.html


### ------------------
### 7. REGISTER USERS
### ------------------


#### 7.1 Register users (employee or employer)









































































































































