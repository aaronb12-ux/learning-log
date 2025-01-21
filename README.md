 # Learning Log

A simple Django web app where you can keep track of things you're learning. You can create an account, add topics you're learning about, and make entries to track your progress.

## What Can You Do?

- Make your own account
- Add topics you're learning
   Write entries about what you learned
- Edit or delete your entries
- Keep everything organized by date

## What's it Built With?

- Django (for the backend)
- Bootstrap (to make it look nice)
- SQLite (for the database)

## How to Run it on Your Computer

1. First, make sure you have Python installed on your computer

2. Download this project:
```bash
git clone https://github.com/yourusername/learning-log.git
cd learning-log
```
3. Set up the virtual enviornment


```bash
#on windows
python -m venv env
env\Scripts\activate
```

```bash
#on mac/linux
python -m venv env
source env/bin/activate
```

4. Install the required packages
```bash
pip install -r requirements.txt
```

5. Set up the database
```bash
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

7. Open up the development server at: http://localhost:8000

### How to Use:
1. Click "Register" to create an account
2. Log in with your new account
3. Click "Add new topic" to start a new learning topic
4. Click on your topic to add entries about what you've learned
5. You can edit or delete entries anytime

### Thank you for reading!
