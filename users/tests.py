from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Department

class UserModelTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.department = Department.objects.create(name="Test Department")

    def test_create_customer(self):
        """Test creating a customer user"""
        user = self.User.objects.create_user(
            username='testcustomer',
            email='customer@test.com',
            password='testpass123',
            role='CUSTOMER'
        )
        self.assertEqual(user.role, 'CUSTOMER')
        self.assertIsNone(user.department)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_employee(self):
        """Test creating an employee user"""
        user = self.User.objects.create_user(
            username='testemployee',
            email='employee@test.com',
            password='testpass123',
            role='EMPLOYEE',
            department=self.department
        )
        self.assertEqual(user.role, 'EMPLOYEE')
        self.assertEqual(user.department, self.department)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_admin(self):
        """Test creating an admin user"""
        user = self.User.objects.create_superuser(
            username='testadmin',
            email='admin@test.com',
            password='testpass123',
            role='ADMIN'
        )
        self.assertEqual(user.role, 'ADMIN')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
