from os.path import abspath, dirname, join

from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))


with open(join(this_dir, "requirements.txt")) as f:
    requirements = f.read().split("\n")

setup(
    name="email_tool",
    version="",
    packages=["email_tool"],
    url="",
    license="",
    author="José Moran",
    author_email="jose.moran@m4x.org",
    description="Simple emailing tool to send notifications from scripts",
    install_requires=requirements,
)
