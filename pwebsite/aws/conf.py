import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from secret_settings import *

# AWS_ACCESS_KEY_ID = "<YOUR AWS ACCESS KEY ID"
# AWS_SECRET_ACCESS_KEY = "<YOUR AWS SECRET KEY>"
# AWS_FILE_EXPIRE = 200
# AWS_PRELOAD_METADATA = True
# AWS_QUERYSTRING_AUTH = False

# DEFAULT_FILE_STORAGE = 'pwebsite.aws.utils.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'pwebsite.aws.utils.StaticRootS3BotoStorage'
# AWS_STORAGE_BUCKET_NAME = '<YOUR AWS BUCKET NAME>'
# S3DIRECT_REGION = 'us-west-1'
# S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_ROOT = MEDIA_URL
# STATIC_URL = S3_URL + 'static/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# two_months = datetime.timedelta(days=61)
# date_two_months_later = datetime.date.today() + two_months
# expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

# AWS_HEADERS = { 
#     'Expires': expires,
#     'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
# }
DEFAULT_FILE_STORAGE = 'pwebsite.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'pwebsite.aws.utils.StaticRootS3BotoStorage'
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = 'maheenportfolio'
AWS_QUERYSTRING_AUTH = False 
# //This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
#static media settings
S3_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_URL = S3_URL + 'media/'
MEDIA_ROOT = MEDIA_URL
#STATIC_URL = S3_URL + 'static/'
# STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )
# STATIC_ROOT = 'staticfiles'
ADMIN_MEDIA_PREFIX = S3_URL + 'admin/'

