import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github_crawler", # Replace with your own username
    version="0.0.6",
    author="Karthik Hosur",
    author_email="karthikhosur15@gmail.com",
    description="A web spider to crawl public github repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthikhosur/Github-Crawler",
    entry_points={
        'console_scripts': ['my-command=github_crawler.main:main']
    },
    packages=setuptools.find_packages(),
    install_requires =[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.6',
)
