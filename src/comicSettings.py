from django.conf import settings

settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,
	DATABASES = {
		'prod': {
			'ENGINE': 'mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': '',                      # Or path to database file if using sqlite3.
			'USER': '',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		},
		'default': {
			'ENGINE': 'mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'comicdb',                      # Or path to database file if using sqlite3.
			'USER': 'root',                      # Not used with sqlite3.
			'PASSWORD': 'root',                  # Not used with sqlite3.
			'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	})	

