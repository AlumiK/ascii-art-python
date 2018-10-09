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
usage: ascii_art.py [-h] [-c CHARSET] [-r RATIO] [-m MAX_SIZE] IMG

create beautiful ascii arts

positional arguments:
  IMG                   original image

optional arguments:
  -h, --help            show this help message and exit
  -c CHARSET, --charset CHARSET
                        set the charset used in the output
  -r RATIO, --ratio RATIO
                        set image aspect ratio
  -m MAX_SIZE, --max-size MAX_SIZE
                        set the max size of the output
```

默认输出到控制台，也可以使用 `> file` 的形式输出到文件。
