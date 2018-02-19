# fortinetProject

written using python3 and django.

to run project: 
1) navigate to dir threatapp, run python manage.py server
2) can go to http://localhost:8000/threatapp/
3) a table with current data is displayed on that index page
4) user can upload json file containing metarecords or 
   directly put json files into the media directory
5) window alert will pop up if table is updated
6) if go to http://localhost:8000/admin/ and login using username/pw: admin/Admin123
   can view sortable table by clicking into threats (was going to implement sorting
   in custom template, but didn't have time)