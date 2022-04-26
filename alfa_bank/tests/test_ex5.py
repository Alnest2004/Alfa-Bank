# import pytest
#
# from internet_banking.models import Loans
#
#
# @pytest.mark.parametrize(
#     "account, credit_amount, paid_out, time",
#     [
#         (1, "132.33", "32", "4"),
#         (1, "177.33", "77", "7"),
#     ],
# )
# def test_loan_instance(
#         db, loan_factory, account, credit_amount, paid_out, time
# ):
#     test = loan_factory(
#         account_id = account,
#         Credit_amount = credit_amount,
#         Paid_out = paid_out,
#         time = time,
#     )
#
#     item = Loans.objects.all().count()
#     assert item == 2
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
