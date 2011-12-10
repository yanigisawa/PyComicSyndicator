from django.conf import settings
import os

os.environ['TZ'] = "US/Eastern"

settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': ':memory:',                      # Or path to database file if using sqlite3.
		}
	})	

