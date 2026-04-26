from faker import Faker

fake = Faker()

VALID_USERNAME = 'standard_user'
VALID_PASSWORD = 'secret_sauce'

INVALID_USERNAME = fake.user_name()
INVALID_PASSWORD = fake.password()

LOCKEDOUT_USERNAME= 'locked_out_user'
LOCKEDOUT_PASSWORD = 'secret_sauce'