# ASCII 字符画

项目基于 [Python](https://www.python.org/) 制作。

## 前置要求

该脚本依赖于 pillow 库。使用以下命令安装。

```
pip install pillow
```

## 使用说明

### 直接运行

使用 `-h|--help` 参数查看使用说明。

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
                        set the aspect ratio of the image
  -m MAX_SIZE, --max-size MAX_SIZE
                        set the max size of the output
```

默认输出到控制台，也可以使用 `> file` 的形式输出到文件。

### 作为模块导入

```python
import ascii_art
```

可用接口如下。

- ascii_art.to_grayscale(infile, max_size, ratio)

    `infile` 输入文件路径。

    `max_size` 长宽最大尺寸（像素）。

    `ratio` 比例。

    将输入图片转换为指定大小和比例的灰度图片。

- ascii_art.make_art(img, charset=default_charset)
  
    `img` 灰度图片。

    `charset` 字符集，默认值为 ``$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. `` 。

    将灰度图片转换为字符画矩阵。

- ascii_art.print_art(art)

    `art` 字符画矩阵。

    打印字符画到标准输出。
