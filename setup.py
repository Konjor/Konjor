try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="konjor",
    version="0.0.1",
    include_package_data=True,
    description="Abstraction library for working with AI",
    author="Tyler Lastovich",
    author_email="hello@konjor.com",
    url="https://github.com/Konjor/konjor",
    packages=["konjor-py"],
    license="",
    keywords=["NLP", "machine learning", "prompts", "low code"],
    install_requires=[
        "analytics-python",
        "fastapi",
        "requests",
    ],
)
