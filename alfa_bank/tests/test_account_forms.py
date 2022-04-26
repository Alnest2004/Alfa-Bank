import factory
import pytest

from internet_banking.forms import CreateTransferForm
from internet_banking.models import Transfer
from tests.factories import UserFactory, User2Factory
from users.forms import RegisterUserForm
from users.models import User



# @pytest.mark.parametrize(
#     "username, email, password1, password2, validity",
#     [
#         ("user1", "test@gmail.com", "poiuytrewq123", "poiuytrewq123", True),
#         ("user1", "test@gmail.com", "poiuytrewq123", "", False),
#         ("user1", "test@gmail.com", "", "poiuytrewq123", False),
#         ("user1", "test@gmail.com", "poiuytrewq123", "poiuytrewq", False),
#         ("user1", "test@.com", "poiuytrewq123", "poiuytrewq123", False),
#     ],
# )
# @pytest.mark.django_db
# def test_create_user(username, email, password1, password2, validity):
#     form = RegisterUserForm(
#         data = {
#             "username": username,
#             "email": email,
#             "password1": password1,
#             "password2": password2,
#         },
#     )
#
#     f = form.errors.as_data()
#     print(f)
#
#     assert form.is_valid() is validity
#
# @pytest.mark.parametrize(
#     "username, email, password1, password2, validity",
#     [
#         ("user1", "test@gmail.com", "poiuytrewq123", "poiuytrewq123", 200),
#         ("user1", "test@gmail.com", "poiuytrewq123", "poiuytrewq", 200), # должно конечно выбивать ошибку, но из-за того,
#         # что у меня есть валидация от django форм и своя собственая, ошибка из-за этого не выбивается, а просто возвращает
#         # эту же страничку с допущенными ошибками, выходит что и status_code будет нормальным(200)
#         ("user1", "", "poiuytrewq123", "poiuytrewq", 200),
#     ],
# )
# @pytest.mark.django_db
# def test_create_account_view(client, username, email, password1, password2, validity):
#     response = client.post(
#         "/authorization/register/",
#         data = {
#             "username": username,
#             "email": email,
#             "password1": password1,
#             "password2": password2,
#         },
#     )
#
#     assert response.status_code == validity
#
#



@pytest.mark.parametrize(
    "from_account, commission, amount, to_account, validity",
    [
        (1, "1.2", "12.22", 2, True),
        (2, "1.2", "-5", 1, False),
        # ("user1", "1.2", "12.22", "user1", False),
    ],
)
def test_transfer(db, account_factory, account2_factory, from_account, commission, amount, to_account, validity):
    acc = account_factory(
        balance = "5",
        user = factory.SubFactory(UserFactory)
    )
    acc2 = account2_factory(
        balance = "100",
        user = factory.SubFactory(User2Factory)
    )
    form = CreateTransferForm(
        data = {
            "from_account": acc,
            "commission": commission,
            "amount": amount,
            "to_account": acc2,
        },
    )

    f = form.errors.as_data()
    print(f)
    print(acc.balance)
    print(acc2.balance)
    assert form.is_valid() is validity


# @pytest.mark.django_db
# def test_user_register_redirect(client):
#     user = User.objects.create_user('test', 'test@test.com', 'test')
#     client.force_login(user)
#     response = client.get("/authorization/register/")
#     assert response.status_code == 200
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
