import setuptools

with open('readme.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='pyfuck',
    version='0.0.1',
    description="Brainfuck interpreter written in Python.",
    long_description=long_description,
    author="LemonPi314",
    author_email='49930425+LemonPi314@users.noreply.github.com',
    url='https://github.com/LemonPi314/fuck',
    license='MIT',
    long_description_content_type='text/markdown',
    keywords=['brainfuck', 'esoteric', 'interpreter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.10.0'
)
