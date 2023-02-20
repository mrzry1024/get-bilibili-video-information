# -*- coding: utf-8 -*-
"""
@Author  : mrzry
@File    : bili.py
@Time    : 2023/02/20
@Blog    : https://www.mrzry.top/
@Desc    : 获取B站分集视频信息
"""

import getopt
import sys
from urllib.parse import urlsplit
import requests
import re
import json

help_document = '''
参数：
-u: 必选  视频链接
-p: 可选  视频集数，默认全部
            -p 5       从第5集开始到最后
            -p 5:10    从第5集到第10集
-f: 可选  将运行输出内容保存到本地文件
-h: 可选  帮助文档

示例：
python bili.py -u "https://www.bilibili.com/video/BV1gr4y1U7CY/" -p 24 -f ./docker学习.txt
'''


def get_info(url):
    """根据url获取视频信息

    :param url: 视频url
    :return:
        - url: 视频url
        - title: 视频标题
        - owner: up主
        - videos: 视频信息
    """
    url = 'https://www.bilibili.com' + urlsplit(url).path
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            data = json.loads(re.findall('window.__INITIAL_STATE__=(.*?);', html)[0])
            videoData = data['videoData']
            title = videoData['title']
            owner = videoData['owner']['name']
            pages = videoData['pages']

            videos = []
            for page in pages:
                video = {'name': page['part'], 'duration': page['duration']}
                videos.append(video)

            return url, title, owner, videos
        else:
            print('请检查网络是否连接以及视频url是否正确')
            sys.exit()
    except SystemExit:
        sys.exit()
    except:
        print('请检查网络是否连接以及视频url是否正确')
        sys.exit()


def output(info, p, output_file):
    """输出视频信息

    :param info: 视频信息
    :param p: 分集数
    :param output_file: 输出文件路径
    :return:
    """
    url, title, owner, videos = info
    content = ''
    content += f'url: {url}\n'
    content += f'标题: {title}\n'
    content += f'up主: {owner}\n'

    p_start, p_end = 0, len(videos)
    if p is not None:
        if ':' in p:
            p_lst = p.split(':')
            p_start = int(p_lst[0]) - 1
            p_end = int(p_lst[1]) - 1
        else:
            p_start = int(p) - 1

    total_duration = 0
    videos_info = '{:<3}{:>8}    {}\n'.format('集数', '时长', '视频')
    for i in range(p_start, p_end):
        duration = videos[i]['duration']
        total_duration += duration
        videos_info += '{:<5d}{:>10}    {}\n'.format(i + 1, convert_duration(duration), videos[i]['name'])
    content += f'总时长: {convert_duration(total_duration)}\n'

    if output_file is not None:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
            f.write(videos_info)
            print(f'已保存到 {output_file}')
    else:
        print(content)
        print(videos_info)


def convert_duration(duration):
    """转换时间格式

    :param duration: 时间秒数
    :return: [HH:]mm:ss
    """
    duration = int(duration)
    h = duration // 3600
    m = (duration - h * 3600) // 60
    s = (duration - h * 3600 - m * 60) % 60
    if h == 0:
        return '{:0>2d}:{:0>2d}'.format(m, s)
    else:
        return '{:0>2d}:{:0>2d}:{:0>2d}'.format(h, m, s)


def main(argv):
    flag = True
    try:
        opts, args = getopt.getopt(argv, 'u:p:f:h')
    except getopt.GetoptError:
        print(help_document)
        sys.exit()

    p = None
    output_file = None
    for opt, arg in opts:
        if opt == '-h':
            print(help_document)
            sys.exit()
        elif opt == '-u':
            flag = False
            info = get_info(arg)
        elif opt == '-p':
            p = arg
        elif opt == '-f':
            output_file = arg

    if flag:
        # 没有参数，或没有-u
        print(help_document)
        sys.exit()

    output(info, p, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
