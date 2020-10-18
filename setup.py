from setuptools import setup
setup(
    name='asciiText',
    version='0.0.1',
    description='Generate Beautiful Ascii Text Art',
    py_modules=['generator'],
    install_requires=[
          'BeautifulSoup4',
          'requests'
      ],
    author='JoeVenner'

)
