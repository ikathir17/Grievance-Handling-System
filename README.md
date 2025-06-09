# Grievance Handling System

A comprehensive web-based grievance management system built with Django that allows organizations to efficiently handle and track customer complaints and feedback.

## Features

### User Management
- Role-based access control (Admin, Employee, Customer)
- Secure authentication with CAPTCHA verification
- Department-wise organization
- User profile management

### Grievance Management
- Grievance submission with file attachments
- Status tracking (Received → In Progress → Resolved/Rejected)
- Escalation mechanism for unresolved grievances
- Department-wise assignment
- Real-time notifications

### Feedback System
- Rating system (1-5 stars)
- Comment submission
- Department performance tracking
- Customer satisfaction metrics

### Admin Features
- Dashboard with statistics and analytics
- Department management
- User management
- Grievance monitoring
- Export functionality for reports

## Technical Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap
- **Icons**: Font Awesome

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/grievance-handling-system.git
cd grievance-handling-system
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django==4.2.7
```

4. Navigate to project directory:
```bash
cd grievance_system
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the website at http://127.0.0.1:8000/
2. Log in to the admin interface at http://127.0.0.1:8000/admin/
3. Create departments and user accounts
4. Start managing grievances

## User Roles

### Admin
- Manage departments and users
- Monitor all grievances
- Generate reports
- Handle escalations

### Employee
- View assigned grievances
- Update grievance status
- Submit resolution reports

### Customer
- Submit grievances
- Track grievance status
- Provide feedback
- View grievance history

## Contact

## Kathiresan P
## Email -
kathiresanp80152@gmail.com
## LinkedIn -
www.linkedin.com/in/kathiresan-p-1703k 
