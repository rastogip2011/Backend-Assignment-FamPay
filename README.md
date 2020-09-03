# Backend-Assignment-FamPay

Requirements:

- python 3.6 or above
- django 3.1 (python library)
- json (python library)
- django-background-tasks (python library)

To run:
execute the following commands in separate terminal/ command line, from the root folder:
>> python manage.py process_tasks
>> python manage.py runserver

Then go to the url provided by django.

Functionalities:
1. Background (async) with some interval (default: 100 seconds, can be changed in views.py file) for fetching the latest videos
2. A GET API which renders the stored video data in a paginated response sorted in descending order of published datetime.
3. Automatically updates the key if the quota for one key is over. For this, specify keys in keys.txt file in root folder
4. Dashboard to view the stored videos with searching and sorting options.

Notes:
- Please wait for the background task to populate DB after visiting the site for the first time.