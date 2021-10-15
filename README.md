## Quick Start
# Prequisites:
- Install Python 3.6+  
- Install pipenv: [$python -m pip install --user pipenv] [if Windows: py instead of python]  
- Install node.js  
- Install yarn

# From root folder:
```bash
# Create and enter into a virtual environment. "exit" to exit
pipenv shell
# install Python dependencies
pipenv install

cd a0_django

# Start backend server at localhost:8000
python manage.py runserver
```

# From b0_react:
```bash
# Install Javascript dependencies
yarn

# Start React server at localhost:3000
yarn start

# Access website at localhost:3000
```

## Web Skeleton Overview (What is included)
- Django backend for the database and API (Django REST Framework [DRF] - ignore the GraphQL stuff [schema.py])
- ReactJS frontend set up with SASS (a more organized version of CSS)
- Icons set up with FontAwesome
- Django's Custom User Model set up
- Example database with connected tables and how to do CRUD functionality with DRF, including profile image uploads for the user
- Authorization is set up, including registering, logging in, and logging out. Can't enter the app until you log in
- Authentication is taken care of with JWT's
- A few pages and components are set up with React for a good project organization
- I can go through the skeleton project and leave notes to describe what is happening at each point if that helps
- I can also give some good links for documentation for further research
