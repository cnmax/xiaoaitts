from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='xiaoaitts',
    version='0.0.1',
    author='Max',
    author_email='mr.qchao@gmail.com',
    description='小爱音箱自定义文本朗读',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cnmaxqi/xiaoaitts',
    project_urls={
        'Bug Tracker': 'https://github.com/cnmaxqi/xiaoaitts/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.6',
    install_requires=[
        'requests~=2.23.0',
    ]
)
