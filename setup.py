from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(name='pyhello',
      version='0.1',
      description='The funniest hello world in the world',
      url='https://github.com/ivan-gimenez/pyhello.git',
      author='Ivan Gimenez',
      author_email='ivan.gimenez@example.com',
      license='MIT',
      packages=['pyhello'],
      zip_safe=False,
      install_requires=requirements,
      )
