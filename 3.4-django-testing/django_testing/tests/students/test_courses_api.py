import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create(name = 'Student1')

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_create_course(client, student):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'student': student.id, 'name': 'test course'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_patch_course(client, courses_factory, students_factory):
    students = students_factory(_quantity=1)
    courses = courses_factory(_quantity=1, students=students)

    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Rename'})
    data = response.json()
    
    assert response.status_code == 200
    assert data['name'] == 'Rename'

@pytest.mark.django_db
def test_delete_course(client, courses_factory, students_factory):
    students = students_factory(_quantity=1)
    courses = courses_factory(_quantity=1, students=students)
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count -1

@pytest.mark.django_db
def test_get_course(client, students_factory, courses_factory):
    students = students_factory(_quantity=1)
    courses = courses_factory(_quantity=1, students=students)

    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == courses[0].name

@pytest.mark.django_db
def test_get_lis_course(client, students_factory, courses_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=1, students=students)

    response = client.get(f'/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(courses) == len(data)
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id   

@pytest.mark.django_db
def test_filter_id(client, students_factory, courses_factory):
    students = students_factory(_quantity=2)
    courses = courses_factory(_quantity=2, students=students)

    response = client.get(f'/api/v1/courses/?id={courses[1].id}')
    data = response.json()

    assert response.status_code == 200
    assert data[1]['id'] == courses[1].id

@pytest.mark.django_db
def test_filter_name(client, students_factory, courses_factory):
    students = students_factory(_quantity=5)
    courses = courses_factory(_quantity=5, students=students)

    response = client.get(f'/api/v1/courses/?name={courses[4].name}')
    data = response.json()

    assert response.status_code == 200
    assert data[4]['name'] == courses[4].name