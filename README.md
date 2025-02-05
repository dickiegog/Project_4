# Blog Application - Django Project

## Table of Contents

1. [Project Overview](#project-overview)
2. [User Experience (UX)](#user-experience-ux)
   - [User Stories](#user-stories)
3. [Features](#features)
   - [Implemented Features](#implemented-features)
   - [Future Features](#future-features)
4. [Database Design](#database-design)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
   - [Manual Testing](#manual-testing)
   - [Automated Testing](#automated-testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Project Overview

The **Blog Application** is a fully-featured blog platform built using Django. It allows users to view, comment on, and interact with blog posts. Authenticated users can submit comments, and site administrators can moderate and manage posts and comments via the Django admin panel. The project also includes an "About Me" page with a collaboration request form, where potential collaborators can reach out to the site owner.

## User Experience (UX)

### User Stories

- A list of user stories to explain functionality and how we developed them can be found here:
  (https://github.com/dickiegog/Project_4/issues)

## Features

### Implemented Features

- **Post Detail View**: Displays individual blog posts with the ability to leave, edit, or delete comments.
- **About Me Page**: Contains a form for potential collaborators to reach out to the site owner.
- **Comment System**: Users can leave comments on posts, edit or delete their own comments, and site admins can approve or delete comments.
- **Admin Management**: Site admins can manage posts and comments through the Django admin interface.

### Future Features

- **Comment Notifications**: Users could receive notifications when their comments are approved or replied to.
- **Post Categories**: Posts could be organized by categories or tags for better filtering.

## Database Design

The project uses Django's ORM for database management. The key models are:

- **Post**: Represents a blog post with fields such as `title`, `body`, `author`, `created_on`, `status`, and `slug`.
- **Comment**: Represents a comment left on a blog post with fields such as `post`, `author`, `body`, `approved`, and `created_on`.
- **About**: Represents the content for the "About Me" page.
- **CollaborateRequest**: Stores requests for collaboration, including `name`, `email`, and `message`.

### Diagram

![Database Diagram](assets/P4_Diagram.png)

## User Experience (UX)

### Wireframes

Before development, wireframes were created to plan the layout and structure of key pages. These wireframes served as a guide for implementing the blog interface and navigation.

- **Home Page Wireframe**  
  ![Home Page Wireframe](assets/homePage.jpg)

- **Blog Page Wireframe**  
  ![Blog Page Wireframe](assets/blogPage.jpg)

The final design evolved from these initial wireframes while keeping usability and accessibility in mind.

## Technologies Used

- **Django 4.2.16**: The web framework used to build the application.
- **Python 3.12**: Programming language for backend logic.
- **PostgreSQL**: Database used in production.
- **Bootstrap 5**: Front-end framework for responsive design.
- **Crispy Forms**: Used for styling Django forms.
- **Summernote**: WYSIWYG editor for post creation.
- **Gunicorn**: WSGI HTTP server for serving the Django application.
- **Heroku**: Platform used for deploying the application.
- **GitHub**: Version control and project repository.

## Testing

### **3️⃣ Automated Testing (Python Unit Tests)**

Unit tests were written in `tests.py` to validate core functionality in the **Django app**, ensuring that models, views, and forms behave as expected.

#### **Test File (`tests.py`)**
![Tests.py File](assets/testPY.png)

#### **Test Execution**
The tests were run using:
```bash
python manage.py test my_blog
```
#### **Test Output**
```
Found 17 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.................
----------------------------------------------------------------------
Ran 17 tests in 2.807s

OK
Destroying test database for alias 'default'...
```

#### **Result:**  
✅ **All 17 tests passed successfully.**


### Manual Testing

Testing was performed manually for each section of the site to ensure all features work as expected. Below are the specific test cases documented in a step-wise manner.

#### **Navigation Links**
- **Expected:** Clicking on navigation links should take the user to the corresponding page.
- **Testing:** Clicked each navigation link (Home, About, Register, Login, Logout) and observed the page load.
- **Result:** All links function correctly, taking users to the expected page.
- **Fix:** No fix required.

#### **Commenting System**
- **Expected:** Logged-in users should be able to add, edit, and delete comments. Admins should be able to approve or delete comments.
- **Testing:** Tested adding, editing, and deleting comments with different user roles.
- **Result:** Comments behaved as expected, updating dynamically.
- **Fix:** No fix required.

#### **Forms and Input Validation**
- **Expected:** Forms should validate inputs and prevent submission of empty or incorrect data.
- **Testing:** Entered invalid data (empty fields, incorrect email formats) and observed error messages.
- **Result:** Validation messages appeared correctly.
- **Fix:** No fix required.

---

### **2️⃣ Responsive Design Testing**
The site was tested for responsiveness by manually adjusting the screen size and capturing screenshots.

#### **Tested Screen Sizes:**
- **Mobile**
  ![Mobile View](assets/mobileView.png)
- **Tablet**
  ![Tablet View](assets/tabletView.png)
- **Desktop**
  ![Desktop View](assets/desktopView.png)

#### **Result:**
✅ The layout adjusted correctly across all screen sizes, ensuring a consistent user experience on **mobile, tablet, and desktop** devices.

---

### **3️⃣ Code Validation**
The following validation tools were used:
- **HTML Validation**: W3C Markup Validator  
  ![HTML Validation](assets/HTMLValidator.png)
- **CSS Validation**: W3C CSS Validator  
  ![CSS Validation](assets/CSSValidator.png)
- ### JavaScript Validation

JavaScript was validated using **JSHint**. The following warnings were noted:

- `const`, `let`, and arrow functions (`=>`) flagged as ES6+ syntax.
- Template literals (`` `${variable}` ``) flagged as ES6+ syntax.
- `for...of` loops flagged as ES6+ syntax.

These warnings were **acknowledged but ignored**, as **ES6 is fully supported by modern browsers** and is an intentional choice in this project.

![JSHint ES6 Warnings](assets/JSValidator.png)


---
### Lighthouse Test

The Lighthouse test confirms that the web application meet has top marks for performance, accessibility, best practices, and SEO standards. Django semantics for href may have slightly reduced optimisation for SEO results.

![Lighthouse Test](assets/P4_Lighthouse.png)

### **4️⃣ User Stories & Feature Testing**
Each user story and feature was tested to ensure proper functionality.

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** |
|------------|--------------------|----------------------|------------|
| Register/Login | Users should be able to register and log in. | Created a new user account, logged in, and logged out. | ✅ Passed |
| Comment System | Users should be able to comment on posts. | Added, edited, and deleted comments. | ✅ Passed |
| Navigation | Clicking links should take users to the correct page. | Clicked all navigation links and observed. | ✅ Passed |

---

### **5️⃣ Bug Fixes & Documentation**
#### **Bugs Encountered**
| **Bug** | **Issue** | **Fix Applied** |
|---------|----------|---------------|
| JavaScript ES6 Errors | JSHint flagged `const`, `let`, and `arrow functions` as invalid. | Configured `.jshintrc` to support ES6. |
| Favicon Not Loading | Favicon path incorrect. | Updated `{% static 'images/favicon.ico' %}` in `<head>`. |

#### **Open Issues**
- No major unresolved issues at this time.

---

### **6️⃣ Test Coverage Summary**
- **All buttons and links** tested and working.
- **Forms validated** with correct error handling.
- **Code validated** using W3C tools and JSHint.
- **No major issues** found after fixes.

For more details, refer to the repository: [GitHub Project](https://github.com/dickiegog/Project_4)


## Deployment

### Heroku Deployment

1. Ensure all dependencies are listed in `requirements.txt`:

   ```bash
   pip freeze > requirements.txt
   ```

2. Add `Procfile` to the root directory with the following content:

   ```bash
   web: gunicorn my_project.wsgi:application
   ```

3. Push the code to GitHub.

4. Create a new Heroku app:

   ```bash
   heroku create <app-name>
   ```

5. Set up PostgreSQL as the database:

   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. Set environment variables:

   ```bash
   heroku config:set SECRET_KEY=<your-secret-key>
   heroku config:set DEBUG=False
   ```

7. Push to Heroku:

   ```bash
   git push heroku main
   ```

8. Run database migrations:

   ```bash
   heroku run python manage.py migrate
   ```

9. Collect static files:
   ```bash
   heroku run python manage.py collectstatic
   ```

### Local Deployment

To run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/dickiegog/Project_4.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database and apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Home Page After Succesful Deployment

![Home Page](assets/P4_Home.png)

## Credits

- [FlyUX Project](https://github.com/CarlMurray/flyUX-pp4/blob/main/README.md) provided inspiration for structuring this README.
- The project uses several open-source libraries such as Django, Crispy Forms, and Bootstrap 5.

## Future Features

- Allow users to edit their profiles
- Allow users to like/ react to posts and commnets
- Add "Previous" button to allow users navigate backwards

## Requirements File

```txt
asgiref==3.8.1
crispy-bootstrap5==0.7
dj-database-url==0.5.0
Django==4.2.16
django-allauth==0.57.2
django-crispy-forms==2.3
django-summernote==0.8.20.0
gunicorn==20.1.0
oauthlib==3.2.2
psycopg2==2.9.9
PyJWT==2.9.0
python3-openid==3.2.0
requests-oauthlib==2.0.0
sqlparse==0.5.1
whitenoise==5.3.0
```
