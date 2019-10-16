from setuptools import setup

setup(name='wealthtaxubi',
      version='0.1',
      description=('Analysis and tool showing the effects on ',
                   'wealth inequality of a wealth-tax-funded UBI.'),
      url='http://github.com/UBICenter/wealth-tax-ubi',
      author='Max Ghenis',
      author_email='max@ubicenter.org',
      license='MIT',
      packages=['wealthtaxubi'],
      install_requires=[
          'microdf',
          'numpy',
          'pandas',
      ],
      zip_safe=False)
