from setuptools import setup, find_packages
""" Minimal setup file for trivia_game project. """
setup(
    name='trivia_game',
    version='0.1.0',
    description=' Answer trivia questions in science, sports, rock and pop',
    packages=find_packages('src'),
    entry_points={
        'console_scripts' : ['trivia_game=trivia_game.cli:main'],
    },

    # metadata
    author='Michael Issa',
    author_email='michael.f.issa@gmail.com',
    license='public',
    install_requires=['pytest']
)