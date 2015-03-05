try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python implementation of osbash',
    'author': 'Pranav Salunke', 'Sayali Lunkad'
    'url': 'https://github.com/sayalilunkad/StackTrain',
    'download_url': 'n/a',
    'author_email': 'dguitarbite@gmail.com', 'sayali.92720@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['stacktrain'],
    'scripts': [],
    'name': 'StackTrain'
}

setup(**config)

