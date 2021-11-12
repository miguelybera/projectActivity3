from setuptools import setup, find_packages

setup(
    name="MapQuestEnhancement",
    version="0.1.2",
    author="Sentinels",
    author_email="sentinels@gmail.com",
    url="https://github.com/miguelybera/projectActivity3",
    description="An application that will enable user to find routes between two locations and be shown necessary trip information.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["MapQuestEnhancement = src.MapQuestEnhancement:MapQuestEnhancement"]},
)