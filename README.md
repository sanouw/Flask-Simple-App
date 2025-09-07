# Flask Simple App

A beginner-friendly Flask web application for user login and registration, with user data stored in a JSON file. This project demonstrates basic Flask routing, HTML templating, static file serving, and simple data persistence.

## Features

- User login form with styled interface
- User registration: saves username and password to `users.json`
- HTML templates for login and index pages
- CSS styling via Flask's static file serving
- Simple, readable code for learning Flask basics

## Project Structure

```
Flask-Course/
├── app.py                # Main Flask application
├── users.json            # Stores registered users
├── static/
│   └── login.css         # CSS for login form
├── templates/
│   ├── index.html        # Home page template
│   └── login.html        # Login form template
└── .gitignore            # Git ignore file
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/MYounus-Codes/Flask-Simple-App.git
   cd Flask-Simple-App
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install flask
   ```

### Running the App
1. **Start the Flask server:**
   ```sh
   python app.py
   ```
2. **Open your browser and go to:**
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
- **Login Page:**
  - Enter a username and password, then submit the form.
  - The credentials are saved to `users.json`.
- **Home Page:**
  - Displays a welcome message after login.

## Customization
- **Styling:**
  - Edit `static/login.css` to change the look and feel of the login form.
- **Templates:**
  - Modify `templates/login.html` and `templates/index.html` for custom content.
- **User Data:**
  - User data is stored in plain text in `users.json`. For production, use a database and hash passwords.

## Security Notice
This project is for educational purposes only. Passwords are stored in plain text and there is no authentication or validation. Do not use this code in production environments.

## Troubleshooting
- **CSS not loading?**
  - Ensure your CSS file is in the `static` folder and linked using `{{ url_for('static', filename='login.css') }}` in your HTML.
- **Template errors?**
  - Make sure your HTML files are in the `templates` folder.
- **JSON errors?**
  - If `users.json` is empty or corrupted, delete it and let the app recreate it.

## License
MIT License

## Author
- [MYounus-Codes](https://github.com/MYounus-Codes)

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
