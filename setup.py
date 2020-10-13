
from setuptools import setup, find_packages
from voltagemetricspublisher.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='voltagemetricspublisher',
    version=VERSION,
    description='Console Application to publish Voltage Metrics to Kafka.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Sumuditha Ranawaka',
    author_email='sumuditha.ranawaka@gmail.com',
    url='https://github.com/SumudithaR/svc.voltage-metrics-publisher',
    license='Apache License 2.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'voltagemetricspublisher': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        voltagemetricspublisher = voltagemetricspublisher.main:main
    """,
)
