import pytest

from users.models import User


# Это так сказать первый этап в тестировании "Получение данных для тестирования"
# или по-другому Arrange. Всего 3 этапа: Arrange; Act; Assert.
# Act - это получается выполнения каких-либо действие. Ну и Assert проверка на совпадение результата
# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")
#
#
# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True
#

# def test_set_check_password1(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"
#
# def test_set_check_password2(user_1):
#     print('check-user2')
#     assert user_1.username == "test-user"
#
# def test_new_user(new_user1):
#     print(new_user1.is_staff)
#     assert new_user1.is_staff

# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.build()
#     count = User.objects.all().count()
#     print(count)
#     print(user.username)
#     assert True
#
# @pytest.mark.django_db
# def test_transfer(db, transfer_factory):
#     transfer = transfer_factory.create()
#     print(transfer.to_account)
#     assert True






