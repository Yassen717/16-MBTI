# 🧠 MBTI Personality Types Explorer

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern web application built with Django that explores and visualizes the 16 Myers-Briggs Type Indicator (MBTI) personality types with interactive charts and detailed trait analysis.

## 🌟 Features

- **📊 Interactive Charts**: Visual representation of personality traits using D3.js circular charts
- **🎨 Modern UI**: Clean, responsive design with Tailwind CSS
- **🔍 Detailed Profiles**: In-depth information about each MBTI type
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **⚡ Fast Performance**: Optimized Django views and database queries
- **🎯 Trait Analysis**: Logic, Imagination, and Discipline scoring for each type

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mbti-personality-explorer.git
   cd mbti-personality-explorer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 📁 Project Structure

```
mbti-personality-explorer/
├── 📁 mbti/                    # Main Django app
│   ├── 📁 templates/           # HTML templates
│   │   ├── 📁 components/      # Reusable components
│   │   └── 📁 pages/          # Page templates
│   ├── 📄 models.py           # MBTI data models
│   ├── 📄 views.py            # View logic
│   ├── 📄 urls.py             # URL routing
│   └── 📄 admin.py            # Admin interface
├── 📁 project/                # Django project settings
│   ├── 📄 settings.py         # Project configuration
│   ├── 📄 urls.py             # Main URL routing
│   └── 📄 wsgi.py             # WSGI configuration
├── 📄 manage.py               # Django management script
├── 📄 requirements.txt         # Python dependencies
└── 📄 README.md               # This file
```

## 🎯 Usage

### Home Page
- **📍 URL**: `/`
- **📋 Description**: Displays all 16 MBTI types in a grid layout
- **🎨 Features**: Interactive circular charts showing trait scores

### MBTI Detail Page
- **📍 URL**: `/mbti/<id>/`
- **📋 Description**: Detailed view of a specific MBTI type
- **🎨 Features**: Comprehensive information and trait breakdown

### About Page
- **📍 URL**: `/about/`
- **📋 Description**: Information about the project and MBTI theory

## 🛠️ Technology Stack

- **🐍 Backend**: Django 4.2+
- **🎨 Frontend**: HTML5, CSS3, JavaScript
- **📊 Charts**: D3.js for interactive visualizations
- **🎨 Styling**: Tailwind CSS for modern design
- **🗄️ Database**: SQLite (development), PostgreSQL (production ready)
- **🔧 Development**: Python virtual environments

## 📊 MBTI Types Supported

The application includes all 16 MBTI personality types:

| Type | Description | Logic | Imagination | Discipline |
|------|-------------|-------|-------------|------------|
| INFP | The Mediator | 65 | 90 | 45 |
| ENFP | The Campaigner | 70 | 85 | 50 |
| INFJ | The Advocate | 75 | 80 | 60 |
| ENFJ | The Protagonist | 80 | 75 | 65 |
| INTP | The Logician | 95 | 70 | 40 |
| ENTP | The Debater | 90 | 75 | 45 |
| INTJ | The Architect | 90 | 65 | 80 |
| ENTJ | The Commander | 85 | 60 | 85 |
| ISFP | The Adventurer | 60 | 75 | 55 |
| ESFP | The Entertainer | 55 | 80 | 50 |
| ISFJ | The Defender | 70 | 60 | 75 |
| ESFJ | The Consul | 65 | 55 | 80 |
| ISTP | The Virtuoso | 85 | 65 | 70 |
| ESTP | The Entrepreneur | 80 | 70 | 65 |
| ISTJ | The Logistician | 90 | 50 | 90 |
| ESTJ | The Executive | 85 | 45 | 95 |

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Database Management
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database
python manage.py flush
```

### Static Files
```bash
python manage.py collectstatic
```

## 🚀 Deployment

### Production Setup

1. **Set environment variables**
   ```bash
   export DJANGO_SETTINGS_MODULE=project.settings
   export DEBUG=False
   export SECRET_KEY=your-secret-key
   ```

2. **Install production dependencies**
   ```bash
   pip install gunicorn
   ```

3. **Configure your web server** (Nginx/Apache)

4. **Run with Gunicorn**
   ```bash
   gunicorn project.wsgi:application
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- 📝 Follow PEP 8 for Python code
- 🎨 Use meaningful commit messages
- 🧪 Write tests for new features
- 📚 Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Myers & Briggs Foundation** for MBTI theory
- **Django Software Foundation** for the amazing web framework
- **D3.js** for interactive data visualization
- **Tailwind CSS** for the beautiful styling framework

## 📞 Support

If you have any questions or need help:

- 🐛 **Report bugs**: [GitHub Issues](https://github.com/yourusername/mbti-personality-explorer/issues)
- 💡 **Request features**: [GitHub Issues](https://github.com/yourusername/mbti-personality-explorer/issues)
- 📧 **Contact**: your.email@example.com

---

<div align="center">
  <p>Made with ❤️ by [Your Name]</p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div> 