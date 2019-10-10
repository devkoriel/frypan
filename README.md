# frypan

## Pre-requisites

- `requests`
- `lxml`

```shell
$ pip install -r requirements.txt
```

or

```shell
$ pip install requests
$ pip install lxml
```

## Usage

```python
>>> import frypan
>>> frypan.isSpam("https://unurl.kr/99a7", ["tvtv24.com"], 2)
True
```