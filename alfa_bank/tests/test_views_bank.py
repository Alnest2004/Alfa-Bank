# import pytest
# # если хотим запустить только одну функциюю на тестирование:
# # pytest tests/test_views_bank.py::test_example
#
# # Тут выполняются все действия перед основными тестами. Например получение всех данных для тестирования.
# # Параметр scope указывает как и сколько раз должна вызываться эта функция
# # --смотреть документацию--.
# @pytest.fixture(scope="session")
# def fixture_1():
#     print('run-fixture-1')
#     return 1
#
# def test_examole1(fixture_1):
#     print('run-example-1')
#     num = fixture_1
#     assert num == 1
#
# # указывает название маркера и строку что он делает.
# # И для запуска с маркером нужно указывать -m. pytest -m "slow"
# @pytest.mark.slow
# def test_example():
#     print("test")
#     assert 1 == 1
#
# def test_example1():
#     assert 1 == 1