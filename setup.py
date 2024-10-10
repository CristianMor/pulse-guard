from setuptools import setup, find_packages

setup(
    name="pulse-guard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'Click',
        'Rich',
        'Inquirer',
        'Python-dotenv',
        'Yaspin'
    ],
    entry_points={
        'console_scripts': [
            'pulse-guard=tool.cli:main',
        ],
    },
)
