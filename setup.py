from setuptools import setup

setup(
    name='pythonapp',
    packages=['pythonapp'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_wtf'
    ],
)
