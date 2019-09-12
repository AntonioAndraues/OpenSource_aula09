from setuptools import setup
setup(name='my_hello_antoniojaj',
      version='0.1',
      packages=['my_hello'],
      python_requires='>=2.7',
      install_requires=[
          'numpy'
      ],
      description='Testing pip distribution',
      author='Antonio Andraues',
      author_email='antoniojaa@al.insper.edu.br',
      license='MIT',
      # The project's main homepage.
      url='https://github.com/AntonioAndraues/OpenSource_aula09/',
      keywords=['testing'],
      scripts=['scripts/hello.py']
      )
