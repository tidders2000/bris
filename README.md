
[![Build Status](https://travis-ci.org/tidders2000/bris.svg?branch=master)](https://travis-ci.org/tidders2000/bris)
BRIS

 BRIS is a light HR system which handle resource management. It could easily be scaled up to a full HR app by
 adding recruitment, onboarding, leaver forms and relations management. The app is aimed at small and medium sized business

 This is a django app that track human resource. shifts are allocated to individuals. Over time and leave
 is requested via the app with online approval. This information will then generate daily rotas for team. There
 is also functionality to manage time in lieu and absence reporting. By using online approval there is no need fortime consumming paper forms
 
 The app genberates a number of exception reports which can be used for payroll purposes. The main estalbishment report
 shows your budgeted against actual for hours used.




User Stories

Overtime can be entered and approved online and an exception report printed for payroll

Holidays can be requested and approved online

Pot hours can be added and approved online

Staff rotas will generate automatically

The system requires authorisation and groups

Reports can be printed to pDF

Hours actual vs used can be compared monthly

Site is reponsive for basic users

Establishement shifts can be allocated to staff

Absence forms can be added and edited online

Managers can see staff who are off sick

A sickness report can be printed monthly for payroll




Features
Existing Features
-Login pages requires e mail and password or users can create themselves.

-Site is reponsive

User can upload images and view stock and sales. Users can select an event from a list of current database entries or add a new one in the same field

User can view images by events. A drop down list of events in the database is provided for selection

Users images are automatically watermarked. I have done this using Pillow after trying a JS solution. This works well but results in two images. I feel there may be a better solution although this one works. In order to implement in production I had to save the image locally then move to S3 using Boto3

signup. Users get sent an email confirmation when they signup.

Django auth handles user management

Users purchase and image and can view their downloads however once this is deleted by the owner it will be removed from the page. A potential archving solution may be required for a later release

sign up form on index footer linked to model to store data but no current functionality to view or use data

Features Left to Implement
-Develop a mechanism to work out commission on sales

-collect user bank information for transfer of income and mechanism to manage transfers

-Add pagination to the search pages

Develop user dashboard for performance report

Add functionality for users to edit e mail sign up settings

Hide menu items that are only applicable to logged in users

Technologies Used
Django for main build - https://www.djangoproject.com
Bootstrap 4 for CSS layout - https://getbootstrap.com/docs/4.0/getting-started/introduction/

Python for coding https://www.python.org/
BOTO3 for uploading media to s3 - https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
jQuery for page interaction: https://jquery.com/

postgres for database- https://www.postgresql.org/
dj-database for postgres and django link up - https://pypi.org/project/dj-database-url/
Gunicorn for production web server - https://gunicorn.org/
bootstrap forms to layout model forms - https://pypi.org/project/django-bootstrap-form/

various django plugins including forms, Auth, Messages
Travis for integration testing - https://travis-ci.org/
Unittest for automated testing
SQLlite3 for development database
GIT for version control

