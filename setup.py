import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='bonsancon-pyblaze',
    version='0.0.9',
    author='Álvaro Ferreira Pires de Paiva',
    author_email='alvarofepipa@gmail.com',
    description='Blaze API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bonsancon/pyblaze',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
