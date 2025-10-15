# Museum Garden - Full-Stack Django Web Application

A comprehensive, full-stack web application developed with Python and the Django Framework. This project serves as a portfolio piece to showcase proficiency in key backend development concepts, from database design to advanced user authentication.

<br>

## Live Demo (Project Showcase)

[![Project Demo GIF](https://github.com/mehranmohammadiii/Museum-Garden-Django/blob/master/assets/gif1.gif)](https://www.linkedin.com/posts/mehran-mohammadi-ceo_django-python-backenddevelopment-activity-7384176820071460864-fXNm?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEwH1a0BGKsjNhnLzWNd2eE1tPo4YlxnGT4)
*(Click the GIF above to watch the full video showcase on LinkedIn)*

---

## 📸 Screenshots

| Home Page                                   | Articles List                                    | Workshop Details                                   |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------- |
| ![Home Page Screenshot](https://github.com/mehranmohammadiii/Museum-Garden-Django/blob/master/assets/Screenshot%20from%202025-10-15%2017-45-34.png) | ![Articles List Screenshot](https://github.com/mehranmohammadiii/Museum-Garden-Django/blob/master/assets/Screenshot%20from%202025-10-15%2017-46-24.png) | ![Workshop Details Screenshot](https://github.com/mehranmohammadiii/Museum-Garden-Django/blob/master/assets/Screenshot%20from%202025-10-15%2017-47-03.png) |

*(Add more beautiful screenshots of the project here)*

---

## ✨ Key Features

- **Dynamic Content Management:** Separate, fully functional apps for Articles, Workshops, Visitor Memories, and more.
- **Role-Based Access Control:** Certain actions, like posting a memory or contacting the museum, are restricted to authenticated users.
- **Advanced User Authentication:** Complete user lifecycle management including registration, login, and logout, built upon Django's secure authentication system.
- **Custom Password Validation:** Enhanced security with custom, localized error messages for password policies.
- **Complex Form Handling:**
    - Creation of memories with simultaneous multi-image uploads.
    - Implemented using a combination of `ModelForm` and `inlineformset_factory`.
- **Intelligent Search:** A unified search feature allowing users to query across multiple models (Articles and Workshops) simultaneously.
- **Responsive Frontend:** A clean, modern, and fully responsive user interface designed with Bootstrap 5.

---

## 🛠️ Tech Stack & Core Concepts Demonstrated

This project leverages a range of technologies and demonstrates a deep understanding of modern web development practices:

- **Backend:** Python, Django, Django REST Framework (future-ready)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Database:** SQLite3 (development), PostgreSQL (production-ready)
- **Core Django Concepts:**
    - **ORM Mastery:**
        - Relational database design using `ForeignKey` and `ManyToManyField`.
        - Performance optimization with `select_related` and `prefetch_related` to mitigate the N+1 query problem.
        - Secure, atomic database updates using `F()` expressions for counters.
    - **Class-Based Views (CBVs):**
        - Implementation of `ListView`, `DetailView`, and `CreateView` for clean, reusable, and extensible code.
        - Overriding methods like `get_context_data` and `form_valid` to handle complex logic.
    - **Advanced Form Processing:**
        - Custom `ModelForm` inheritance to add styles and extra fields.
        - Handling multiple forms on one page with `inlineformset_factory`.
    - **Security:**
        - Protection against CSRF attacks.
        - Secure handling of the `SECRET_KEY` using environment variables (`python-dotenv`).
    - **URL Routing:**
        - App-specific URL configuration using `include()` and `app_name`.
        - Creating user-friendly, SEO-ready URLs with slugs.

---

## 🚀 Local Setup and Installation

Follow these steps to get the project running locally:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` File:**
    Create a `.env` file in the project root and add your `SECRET_KEY`:
    ```    SECRET_KEY='your-secret-key'
    ```

5.  **Run Database Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional):**
    This allows you to access the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The project is now available at `http://127.0.0.1:8000/`.
