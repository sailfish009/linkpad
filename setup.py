from setuptools import setup

setup(
    name='linkpad',
    version='1.2',
    description='A command-line bookmark manager',
    author='Tony Duckles',
    author_email='tony@nynim.org',
    url='https://github.com/tonyduckles/linkpad',
    py_modules=['linkpad'],
    install_requires=[
        'click',
        'pyyaml',
        'sh',
        'bs4',
        'requests',
        'tqdm',
    ],
    license='MIT',
    entry_points="""
        [console_scripts]
        linkpad=linkpad:cli
    """,
)
