import json
import math
import operator
import os
from functools import reduce

import numpy as np
from PIL import Image

import Ocr
import Screenshot


def image_contrast(img1, img2):
    try:
        image1 = Image.open(img1)
        image2 = Image.open(img2)
    except FileNotFoundError:
        raise Exception('找不到文件')
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result


class Character:
    def __init__(self, config_path='character.json'):
        self.title = '原神'
        self.ocr = Ocr.init_ocr()
        self.config_path = config_path
        self.config = self._get_config()
        self._config_mtime = os.stat(self.config_path).st_mtime
        self.all_characters = list(self.config['common'].keys())
        self.special_characters = list(self.config['special'].keys())
        self.index = 0
        self.current_character = ''
        self.delay = 0
        self.bianshen = {'character': '',
                         'flag': False,
                         'duration': 0,
                         'start': 0.0}
        self.mode = 'single'
        self.special_mode = {
            '那维莱特': None,
            '甘雨': 0,
            '胡桃': 0,
            '五郎': None,
            '菲谢尔': None
        }

        self.crop_table = {
            'single': {
                '16:10': [2160, 490, 2355, 560],
                '16:9': [2160, 325, 2355, 395]
            },
            'double': {
                '16:10': [2160, 690, 2355, 760],
                '16:9': [2160, 540, 2355, 610]
            },
            'three': {
                '16:10': [2160, 825, 2355, 895],
                '16:9': [2160, 665, 2355, 735]
            },
            'four': {
                '16:10': [2160, 885, 2355, 955],
                '16:9': [2160, 725, 2355, 795]
            },
            'burst': {
                '16:10': [2350, 1380, 2502, 1550],
                '16:9': [2350, 1220, 2502, 1390]
            }
        }

    def _get_config(self):
        with open(self.config_path, 'r', encoding='gbk') as f:
            config = json.load(f)
        return config

    def update_config(self):
        if os.stat(self.config_path).st_mtime != self._config_mtime:
            with open(self.config_path, 'r', encoding='gbk') as f:
                self.config = json.load(f)
                self._config_mtime = os.stat(self.config_path).st_mtime
                self.all_characters = list(self.config['common'].keys())
                self.special_characters = list(self.config['special'].keys())
            print('config updated')

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def get_current_character(self):
        aspect_ratio = Screenshot.Screenshot.get_aspect_ratio(self.title)
        if self.mode == 'single':
            base_crop = self.crop_table['single'][aspect_ratio]
            step = 128
            crop = [base_crop[0], base_crop[1] + step * (self.index - 1), base_crop[2],
                    base_crop[3] + step * (self.index - 1)]
            img = Screenshot.Screenshot.screenshot(crop, self.title)
        elif self.mode == 'double':
            base_crop = self.crop_table['double'][aspect_ratio]
            step = 120
            crop = [base_crop[0], base_crop[1] + step * (self.index - 1), base_crop[2],
                    base_crop[3] + step * (self.index - 1)]
            img = Screenshot.Screenshot.screenshot(crop, self.title)
        else:
            base_crop = self.crop_table[self.mode][aspect_ratio]
            crop = base_crop
            img = Screenshot.Screenshot.screenshot(crop, self.title)
        # with open('test.png', 'wb') as f:
        #     img.save(f)
        img = np.array(img)
        self.current_character = Ocr.Ocr(self.ocr, img)

    def is_burst(self):
        aspect_ratio = Screenshot.Screenshot.get_aspect_ratio(self.title)
        crop = self.crop_table['burst'][aspect_ratio]
        test = Screenshot.Screenshot.screenshot(crop, self.title)
        with open('burst/{}_test.png'.format(self.current_character), 'wb') as f:
            test.save(f)
        test = 'burst/{}_test.png'.format(self.current_character)
        full = 'burst/{}_full.png'.format(self.current_character)
        empty = 'burst/{}_empty.png'.format(self.current_character)
        if image_contrast(test, empty) - image_contrast(test, full) > 100 and image_contrast(test, full) < 300:
            return True
        else:
            return False
