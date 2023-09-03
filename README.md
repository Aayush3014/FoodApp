# Food Menu Listing Web App

This Django-based web application allows users to browse a variety of food items listed in a menu. Users can register, log in, and manage their profiles. Upon registration, a user profile is created, providing a personalized experience. This project aims to simplify the process of exploring a diverse range of delicious food options.

## Features:
- User Registration: Users can sign up using their email and password.
- User Authentication: Registered users can log in securely.
- User Profiles: A unique user profile is created upon registration, allowing users to customize their experience.
- Food Menu: The app displays a curated list of food items.
- User-friendly Interface: The user interface is designed to be intuitive and visually appealing.

## Installation

Follow these steps to set up the project on your local system:

### Prerequisites

- Python 3.x installed on your machine.
- `pip` package manager installed.

### Clone the Repository

```bash
git clone https://github.com/yourusername/food-menu-listing-web-app.git
```
### Create a Virtual Environment (Optional but Recommended)
```bash
cd food-menu-listing-web-app
python3 -m venv venv
```

## Activate the Virtual Environment

On Windows
```bash
venv\Scripts\activate
```
On macOS and Linux
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Database Setup

Create the database and apply migrations:
```bash
python3 manage.py migrate
```

### Create a Superuser

You can create a superuser to manage the admin panel:
```bash
python3 manage.py createsuperuser
```

### Start the Development Server

```bash
python3 manage.py runserver
```

The application should now be accessible at http://localhost:8000/ in your web browser.

### Home Page

![Screenshot from 2023-09-04 00-37-57](https://github.com/Aayush3014/FoodApp/assets/83333424/7e716b0d-bd93-443f-85cd-2076013f4c54)


### Register Page

![Screenshot from 2023-09-04 00-39-28](https://github.com/Aayush3014/FoodApp/assets/83333424/04c56118-7d44-412d-9e30-64c5442ad6b3)

### Login Page

![Screenshot from 2023-09-04 00-40-41](https://github.com/Aayush3014/FoodApp/assets/83333424/28913248-97d1-40ad-93a1-94a80e81865d)

### Add Items Page

![Screenshot from 2023-09-04 00-43-40](https://github.com/Aayush3014/FoodApp/assets/83333424/489c6811-990c-499f-8437-607ea112391e)


### Usage

- Visit the website and sign up for a new account or log in with your credentials.
- Explore the food menu and discover delicious options.
- Customize your profile to enhance your experience.

### License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
