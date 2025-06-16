# Django Signup & Login App

This project is a simple Django web application that provides user signup, login, and OTP verification functionality using a custom `UserProfile` model. It is modular and ready to be extended with additional apps.

## Features

- User registration (signup) with username, email, and mobile number
- Secure password hashing
- User login with session management
- OTP (One-Time Password) field for enhanced security (template-ready)
- Modular structure for easy extension

## Project Structure

```
ms_site/                # Django project settings
signup_login/           # Main app for authentication
    models.py
    views.py
    forms.py
    urls.py
    templates/
        base.html
        index.html
        login.html
        signup.html
        otp.html
manage.py
```

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```sh
    pip install django
    ```

3. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Access the app:**
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new user via the Sign Up page.
- Log in with your credentials.
- OTP field is present in the templates for future implementation.

## Customization

- To add more fields or apps, create new Django apps and include them in `INSTALLED_APPS`.
- To implement OTP verification, update the views and forms accordingly.

## License

This project is for educational purposes. You may modify and use it as needed.

---
```# Django Signup & Login App

This project is a simple Django web application that provides user signup, login, and OTP verification functionality using a custom `UserProfile` model. It is modular and ready to be extended with additional apps.

## Features

- User registration (signup) with username, email, and mobile number
- Secure password hashing
- User login with session management
- OTP (One-Time Password) field for enhanced security (template-ready)
- Modular structure for easy extension

## Project Structure

```
ms_site/                # Django project settings
signup_login/           # Main app for authentication
    models.py
    views.py
    forms.py
    urls.py
    templates/
        base.html
        index.html
        login.html
        signup.html
        otp.html
manage.py
```

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```sh
    pip install django
    ```

3. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Access the app:**
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new user via the Sign Up page.
- Log in with your credentials.
- OTP field is present in the templates for future implementation.

## Customization

- To add more fields or apps, create new Django apps and include them in `INSTALLED_APPS`.
- To implement OTP verification, update the views and forms accordingly.

## License

This project is for educational purposes. You may modify and use it as needed.

---
