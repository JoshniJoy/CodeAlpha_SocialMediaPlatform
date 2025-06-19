# LinkLoop: A Social Media Platform

![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship%20Project-blue)
![Technology](https://img.shields.io/badge/Tech-Django%20%7C%20Python%20%7C%20HTML%20%7C%20JS-green)

LinkLoop is a mini social media web application built with Django. This project was developed as a task for the CodeAlpha web development internship. It includes core social media functionalities such as user authentication, creating posts, a live feed, user profiles, and a like/follow system.

## 🔗 Project Demo

Live URL - [Demo link](https://linkloop.pythonanywhere.com/)

---

## ✨ Core Features

*   **User Authentication**: Secure user registration and login system.
*   **User Profiles**: View and edit user profiles with a bio and profile picture.
*   **Create Posts**: Users can create and share short text-based posts.
*   **Interactive Feed**: A central feed displaying posts from followed users and the user's own posts.
*   **Post Details & Comments**: View a single post and add comments.
*   **Like System**: Users can like and unlike posts, with real-time count updates using JavaScript.
*   **Follow/Unfollow System**: Users can follow other users to see their content in the feed.
*   **Responsive UI**: Basic responsiveness for a good experience on different screen sizes using Bootstrap.

---

## 🛠️ Tech Stack

*   **Backend**: Python, Django
*   **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
*   **Database**: SQLite3 (for development)
*   **Version Control**: Git & GitHub

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

*   Python (3.8 or higher)
*   Git

### Installation & Setup

1.  **Clone the repository:**
    *(Note: If you have already cloned it, you can skip this step. If your repository name is different, use the correct URL.)*
    ```sh
    git clone https://github.com/JoshniJoy/LinkLoop.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd LinkLoop
    ```

3.  **Create and activate a virtual environment:**
    *   For Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   For macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Create a superuser to access the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```
    (Follow the prompts to create a username and password)

7.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

---

## 📸 Screenshots

![1](https://github.com/user-attachments/assets/5d88fb55-f94c-4b93-a105-35e0b8907928)

![2](https://github.com/user-attachments/assets/8962bd13-b5d3-45cc-9d6d-98bf5a9d92b6)

![3](https://github.com/user-attachments/assets/46d58b32-c98f-48e3-b96b-f3fff042b7a4)

![4](https://github.com/user-attachments/assets/e8361688-74f7-4fff-a58f-d4336011fe1b)

![5](https://github.com/user-attachments/assets/cbba52cb-4739-4a82-8177-d53aa61b66c3)


---

## 📝 Usage

*   **Sign up** for a new account or **log in** with existing credentials.
*   Create a few different user accounts to test the follow functionality.
*   From the main feed, **create a new post**.
*   Navigate to another user's profile and click the **Follow** button.
*   Go back to your feed to see the posts from the user you just followed.
*   **Like** and **comment** on posts.
*   Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users, posts, and other data directly.

---

## 👤 Contact

Joshni Joy - [GitHub Profile](https://github.com/JoshniJoy)
