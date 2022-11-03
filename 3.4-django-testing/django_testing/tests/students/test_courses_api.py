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
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_create_course(client, student):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'student': student.id, 'name': 'test name'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

# @pytest.mark.django_db
# def test_update_course(client, student, course_factory):
#     сourse = course_factory(_quantity=5)

#     response = client.patch('/api/v1/courses/', data={'student': student.id, 'name': 'test name2'})
#     assert response.status_code == 201
#     data = response.json()
#     assert len(data) == len(сourse)
#     for i, m in enumerate(data):
#         assert m['name'] == сourse[i].name

@pytest.mark.django_db
def test_delete_course(client, student):

    response = client.post('/api/v1/courses/', data={'student': student.id, 'name': 'test name'})
    assert response.status_code == 201
    # count = Course.objects.count()
    
    id = Course.objects.first()
    response = client.patch('/api/v1/courses/', data={'name': 'test name2'}, format = 'json')
    assert response.status_code == 201
    # assert Course.objects.count() == count - 1


    # проверка получения 1го курса (retrieve-логика)
    # создаем курс через фабрику
    # строим урл и делаем запрос через тестовый клиент
    # проверяем, что вернулся именно тот курс, который запрашивали
    # проверка получения списка курсов (list-логика)
    # аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
    # проверка фильтрации списка курсов по id
    # создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
    # проверка фильтрации списка курсов по name

    # тест успешного обновления курса
    # сначала через фабрику создаем, потом обновляем JSON-данными
    # тест успешного удаления курса