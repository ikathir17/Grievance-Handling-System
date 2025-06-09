from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Grievance, Department
from django.utils import timezone

# Create your tests here.

class GrievanceModelTests(TestCase):
    def setUp(self):
        # Create test department
        self.department = Department.objects.create(name="Test Department")
        
        # Create test users
        self.User = get_user_model()
        self.customer = self.User.objects.create_user(
            username='testcustomer',
            email='customer@test.com',
            password='testpass123',
            role='CUSTOMER'
        )
        self.employee = self.User.objects.create_user(
            username='testemployee',
            email='employee@test.com',
            password='testpass123',
            role='EMPLOYEE',
            department=self.department
        )

    def test_create_grievance(self):
        """Test creating a new grievance"""
        grievance = Grievance.objects.create(
            user=self.customer,
            department=self.department,
            description="Test grievance",
            status='RECEIVED'
        )
        self.assertEqual(grievance.status, 'RECEIVED')
        self.assertEqual(grievance.user, self.customer)
        self.assertEqual(grievance.department, self.department)

    def test_grievance_status_update(self):
        """Test updating grievance status"""
        grievance = Grievance.objects.create(
            user=self.customer,
            department=self.department,
            description="Test grievance",
            status='RECEIVED'
        )
        grievance.status = 'IN_PROGRESS'
        grievance.save()
        self.assertEqual(grievance.status, 'IN_PROGRESS')
