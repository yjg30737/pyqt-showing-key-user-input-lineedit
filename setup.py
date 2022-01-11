from setuptools import setup, find_packages

setup(
    name='pyqt-showing-key-user-input-lineedit',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Detect the key which user input and show it on the lineedit.',
    url='https://github.com/yjg30737/pyqt-showing-key-user-input-lineedit.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)