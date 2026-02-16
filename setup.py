from setuptools import setup, find_packages

setup(
    name='my_planner',
    version='0.1.0',
    packages=find_packages("."),
    scripts=["planer_pkg/main.py"],  # Расположение главного исполняемого файла.
    url='https://github.com/Marat-Sirazetdinov/my_planner',  # Адрес репозитория с вашей курсовой работой.
    license='Apache-2.0',
    author='Сиразетдинов Марат Рустамович',
    author_email='marat-sir@mail.ru',
    description='Консольное приложение для структурированного управления личным расписанием.',
    include_package_data=True,
    install_requires=[],

)