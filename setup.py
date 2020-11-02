from setuptools import setup

VERSION = "1.0.0"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="download_or_update_all_github_repos",
    version=VERSION,
    description="Downloads or updates all github repos from a given user",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="Download github repos repo repository repositories",
    url="https://github.com/danilocgsilva/download_or_update_all_github_repos2.git",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["download_or_update_all_github_repos"],
    entry_points={"console_scripts": ["githubdw=download_or_update_all_github_repos.__main__:main"],},
    include_package_data=True
)

