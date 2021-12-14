# money balance 10000
# savings bank 500 and current account 0 minimum balance

money_balance = 10000

# Defining our own customized exception
class Withdraw100Error(Exception):
    pass
class WithdrawSavingsError(Exception):
    pass
class WithdrawCurrentError(Exception):
    pass

account_type = input("Enter your account type?")
while True:
    try:
        withdraw_amount = int(input("Please, enter amount?"))
        if not withdraw_amount%100 ==0:
            # using customized exception
            raise Withdraw100Error("Enter in 100 multiples only!!")
        money_balance-=withdraw_amount
        print(f"Money balance: {money_balance}")
        if money_balance<0 and account_type=="c":
            raise WithdrawCurrentError("Balance should be nagative!!")
        if money_balance<500:
            raise WithdrawSavingsError("Please maintain minimum 500!!")

    except Withdraw100Error as e:
        print(e)

    except WithdrawCurrentError as e:
        print(e)
        break

    except WithdrawSavingsError as e:
        print(e)
        break

    except Exception as e:
        print(e)
