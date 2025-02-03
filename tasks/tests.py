from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(title='Test Task 1', description='Test Description 1', completed=False)

    def test_task_creation(self):
        task = Task.objects.create(title='New Task', description='New Description', completed=True)
        self.assertEqual(task.title, 'New Task')
        self.assertTrue(task.completed)

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {'title': 'Task API', 'description': 'Testing API', 'completed': False}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'completed': True}
        response = self.client.put(f'/api/tasks/{self.task1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task1), 'Test Task 1')

    def test_task_default_status(self):
        task = Task.objects.create(title='Test Default', description='Should be False')
        self.assertFalse(task.completed)

    def test_task_detail_view(self):
        response = self.client.get(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_task_creation(self):
        data = {'description': 'Missing title'}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_task_update(self):
        data = {'title': ''}  # Invalid update with empty title
        response = self.client.put(f'/api/tasks/{self.task1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_ordering(self):
        Task.objects.create(title='Z Task', description='Last task')
        Task.objects.create(title='A Task', description='First task')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

