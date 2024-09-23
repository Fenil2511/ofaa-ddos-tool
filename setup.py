from distutils.core import setup

setup(
    name="OFAA",
    py_modules=["ofaa"],
    entry_points={"console_scripts": ["ofaa=ofaa:main"]},
    version="0.1.0",
    description="Low bandwidth DoS tool.",
    author ="Fenil Om Ayush Aditi",
    url="https://github.com/gkbrk/slowloris",
    keywords=["dos", "http", "ofaa"],
    license="MIT",
)
