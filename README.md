# 字符画

项目基于 [Python](https://www.python.org/) 语言制作。

## 前置要求

该脚本依赖于 pillow 库。使用以下命令安装。

```
pip install pillow
```

## 使用说明

使用 `-h` 参数查看使用说明。

```
> python ascii_art.py -h
usage: ascii_art.py [-h] [-c [CHARSET]] [-r [RATIO]] [-m [MAX_DIM]] IMG

create beautiful ascii arts

positional arguments:
  IMG                   original image

optional arguments:
  -h, --help            show this help message and exit
  -c [CHARSET], --charset [CHARSET]
                        set the charset used in the output
  -r [RATIO], --ratio [RATIO]
                        set image aspect ratio
  -m [MAX_DIM], --max-dim [MAX_DIM]
                        set the max size of the output
```
