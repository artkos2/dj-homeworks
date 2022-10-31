import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def message_factory_student():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def message_factory_course():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()
    response = client.post('/messages/', data={'name': user.id, 'students': 'test text'})

    # Act
    response = client.get('/messages/')

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_create_message(client, user):
    count = Message.objects.count()

    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})

    assert response.status_code == 201
    assert Message.objects.count() == count + 1





    # проверка получения 1го курса (retrieve-логика)
    # создаем курс через фабрику
    # строим урл и делаем запрос через тестовый клиент
    # проверяем, что вернулся именно тот курс, который запрашивали
    # проверка получения списка курсов (list-логика)
    # аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
    # проверка фильтрации списка курсов по id
    # создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
    # проверка фильтрации списка курсов по name
    # тест успешного создания курса
    # здесь фабрика не нужна, готовим JSON-данные и создаем курс
    # тест успешного обновления курса
    # сначала через фабрику создаем, потом обновляем JSON-данными
    # тест успешного удаления курса