from setuptools import find_packages, setup

setup(
    name='django-invitations',
    packages=find_packages(),
    package_data={'invitations': ['templates/*.*']},
    include_package_data=True,
    zip_safe=False,
    version='1.9.6',
    description='Generic invitations app with support for django-allauth',
    author='https://github.com/bee-keeper',
    keywords=['django', 'invitation', 'django-allauth', 'invite'],
)
