# -*- coding: utf-8 -*-
# Created: 3/9/2018
# Project : TomatoClock
from anki.lang import currentLang

ADDON_CD = 1608644302
HAS_SET_UP = False
MIN_SECS = 60
__version__ = "0.1.4"

REST_MINS = 5

UPDATE_LOGS = (
    (
        "0.1.4", u"""
        <ol>
            <li>新增： 静音选项，详细见设置 > PlaySounds</li>
            <li>新增： 插件投票选项（窗口右上角） </li>
            <li>修复： 若干BUG</li>
            </ol>
        """ if currentLang == 'zh_CN' else """
        <ol>
            <li>Added: Mute for sounds, see in settings > PlaySounds </li>
            <li>Added: "Vote for Addon" button, at the top right corner of window </li>
            <li>Fixed: several bugs</li>
            </ol>"""
    ),
)
