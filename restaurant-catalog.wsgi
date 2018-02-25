import sys

sys.path.insert(0, "/var/www/restaurant-catalog/")


from restaurant-catalog import app as application

application.secret_key = 'super_secret_key'

