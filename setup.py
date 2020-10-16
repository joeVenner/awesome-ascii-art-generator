from setuptools import setup
setup(
    name='asciiText',
    version='0.0.1',
    description='Generate Beautiful Ascii Text Art',
    py_modules=['generator'],
    package_dir={'':'src'},
    install_requires=[
          'BeautifulSoup',
          'requests'
      ],
    author='JoeVenner',
    author_mail='ylafrimi@gmail.com'

)