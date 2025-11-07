# Django Blog — Dark Pro Theme

A Django blog featuring:
- Tailwind dark UI with animated cards & pagination
- Summernote rich text editor (images + YouTube/Vimeo)
- YouTube preview fallback (no Error 153)
- Moderated comments

## Quickstart

```bash
python -m venv venv
source venv/Scripts/activate   # on Windows Git Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



shree@shreesh MINGW64 ~
$ ^[[200~cd /c/Users/YourName/Desktop/python
bash: $'\E[200~cd': command not found

shree@shreesh MINGW64 ~
$ cd c
bash: cd: c: No such file or directory

shree@shreesh MINGW64 ~
$ ^C

shree@shreesh MINGW64 ~
$ cd /c/Users/shree/Desktop/python

shree@shreesh MINGW64 ~/Desktop/python
$ ls
index.py  mysite/

shree@shreesh MINGW64 ~/Desktop/python
$ git init
Initialized empty Git repository in C:/Users/shree/Desktop/python/.git/

shree@shreesh MINGW64 ~/Desktop/python (master)
$ git config user.name "ShreeshSKatti"

shree@shreesh MINGW64 ~/Desktop/python (master)
$ git config user.email "shreeshkatti212@gmail.com"

shree@shreesh MINGW64 ~/Desktop/python (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        index.py
        mysite/

nothing added to commit but untracked files present (use "git add" to track)

shree@shreesh MINGW64 ~/Desktop/python (master)
$ cat > .gitignore << 'EOF'
# Byte-compiled / cache
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
env/

# Django
*.log
*.pot
*.pyc
db.sqlite3
media/
staticfiles/
*.sqlite3

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Environment / secrets
.env
.env.*
!.env.example

# Node / front-end (if any)
node_modules/
