from setuptools import setup, find_packages

setup(
    name='chestrays',
    version='0.0.1',
    install_requires=[
        'kaggle',
    ],
    python_requires='>=3.6',
    author='Chestray contributors',
    author_email='chestrays@wildtreetech.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'krun = chestrays.__main__:run',
            'kfetch = chestrays.__main__:fetch',
        ]
    },
)
