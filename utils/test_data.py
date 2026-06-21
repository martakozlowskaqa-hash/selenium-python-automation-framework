from faker import Faker

fake = Faker()

VALID_USERNAME = 'standard_user'
VALID_PASSWORD = 'secret_sauce'

INVALID_USERNAME = fake.user_name()
INVALID_PASSWORD = fake.password()

LOCKEDOUT_USERNAME = 'locked_out_user'
LOCKEDOUT_PASSWORD = 'secret_sauce'

#PRODUCTS
BACKPACK_PRICE = '$29.99'
JACKET_PRICE = '$49.99'
ONESIE_PRICE = '$7.99'

BACKPACK_NAME = 'Sauce Labs Backpack'
JACKET_NAME = 'Sauce Labs Fleece Jacket'
ONESIE_NAME = 'Sauce Labs Onesie'

#CHECKOUT
CHECKOUT_TOTAL = '$32.39'

#ERROR MESSAGES
LOGIN_INVALID_ERROR = 'Epic sadface: Username and password do not match any user in this service'
LOGIN_LOCKED_ERROR = 'Epic sadface: Sorry, this user has been locked out.'

CHECKOUT_FIRSTNAME_ERROR = 'Error: First Name is required'
CHECKOUT_LASTNAME_ERROR = 'Error: Last Name is required'
CHECKOUT_ZIPCODE_ERROR = 'Error: Postal Code is required'