from setuptools import setup, find_packages

setup(
    name='pythonapp',
    packages=find_packages(),
    url='https://bitbucket.org/Terapin_Malik/pythonapp',
    include_package_data=True,
    author_email='malik.abukalokoh@yahoo.com',
    description='Basic application to make a reminder application',
    platforms='any',
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_wtf',
        'flask_migrate',
    ],
)
