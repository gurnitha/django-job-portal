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