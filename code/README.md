### README

## How to run the app?
1. 'git clone'
2. 'cd lighthelper/code'
3. 'virtualenv givelight'
4. 'source givelight/bin/activate'
5. 'pip install -r requirements.txt'
6.  Assume you have PSQL installed. Create a database locally, 'CREATEDB givelight_local' without password.
7.  If you update 'models.py' file, please run 'python models.py db migrate', it will generate a file under /migrations/versions
8.  Then run 'python models.py db upgrade' to sync up your database along with new changes
