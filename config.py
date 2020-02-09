import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"\xf9t\x80kk\x14'\xd5NZ\xdfA\xd1i*\xac"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }