import pytest
import random
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from django.urls import reverse


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make('Course', *args, **kwargs)

    return factory


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make('Student', *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory, student_factory):
    students = student_factory(_quantity=2)
    course = course_factory(students=students)
    url = reverse('courses-detail', args=[course.id])
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id
    assert data['name'] == course.name


@pytest.mark.django_db
def test_get_course_list(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(students=students, _quantity=3)
    courses_id_list = [course.id for course in courses]
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses_id_list)


@pytest.mark.django_db
def test_filter_id_course(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(students=students, _quantity=3)
    random_id = random.choice(courses).id
    url = reverse('courses-list')
    response = client.get(url, {'id': random_id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == random_id


@pytest.mark.django_db
def test_filter_name_course(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(students=students, _quantity=3)
    random_course = random.choice(courses)
    random_id = random_course.id
    random_name = random_course.name
    url = reverse('courses-list')
    response = client.get(url, {'name': random_name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == random_id
    assert data[0]['name'] == random_name


@pytest.mark.django_db
def test_course_create(client):
    course = {'name': 'Math'}
    url = reverse('courses-list')
    response = client.post(url, course)
    response_get = client.get(url, {'name': course['name']})
    assert response.status_code == 201
    assert response_get.status_code == 200
    data = response_get.json()
    assert data[0]['name'] == course['name']


@pytest.mark.django_db
def test_course_update(client, course_factory, student_factory):
    students = student_factory(_quantity=2)
    course = course_factory(students=students)
    course_new = course_factory(students=students)

    url = reverse('courses-detail', args=[course.id])
    course_update = {'name': course_new.name}
    response = client.patch(url, course_update)
    assert response.status_code == 200

    response_get = client.get(url, {'id': course.id})
    assert response_get.status_code == 200
    data = response_get.json()
    assert data['name'] == course_update['name']


@pytest.mark.django_db
def test_course_delete(client, course_factory, student_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(students=students, _quantity=4)
    random_course_id = random.choice(courses).id

    url = reverse('courses-detail', args=[random_course_id])
    response_delete = client.delete(url)
    assert response_delete.status_code == 204

    url_list = reverse('courses-list')
    response_get = client.get(url_list)
    assert response_get.status_code == 200
    data = response_get.json()
    id_list = [course['id'] for course in data]
    assert random_course_id not in id_list
