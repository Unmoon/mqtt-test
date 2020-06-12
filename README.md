# MQTT test
Simple example of multiple clients sending and receiving messages asynchronously.

## Requirements

* Python 3.7+

Virtual environment should be created before installing.
```shell script
python -m venv venv
venv\Scripts\activate
python -m pip install -U pip setuptools
```

## Install in editable mode

`-e` allows editing the application without having to reinstall it.
```shell script
pip install -e .
python -m mqtt-test
```

## Codestyle

This project uses [Black](https://github.com/psf/black) for code formatting.

```shell script
pip install black
black mqtt-test/
black setup.py
```
