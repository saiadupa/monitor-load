from setuptools import setup, find_packages

setup(
    name="monitor-load", 
    version="0.1.0", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'monitor_load = monitor_load.cli:main', 
        ],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nithin Sai Adupa",
    author_email="your-email@example.com",
    description="A CLI tool to monitor system load and pause/resume a process.",
    url="https://github.com/adupa/monitor-load",  
    license="MIT",  # License for your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
