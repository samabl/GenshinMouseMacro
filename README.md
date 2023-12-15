某二次元游戏自动化脚本，作者是新手能力有限，目前只有这些功能，想添加新功能请issue，欢迎大佬PR，觉得好用的话请给个star喵~

## 目录

<!-- TOC -->
* [目录](#目录)
  * [安装](#安装)
  * [运行](#运行)
  * [功能](#功能)
    * [通用](#通用)
    * [特殊角色](#特殊角色)
  * [注意事项](#注意事项)
<!-- TOC -->

## 安装

推荐使用[Python 3.11](https://www.python.org/downloads/release/python-3117/)

在项目目录打开cmd并使用以下命令安装依赖

```shell
pip install -r requirements.txt
```

## 运行

双击`GenshinMacro.py`，选择`使用Python打开`或者在项目目录打开cmd并使用以下命令运行

```shell
python GenshinMacro.py
```

首次运行前需要修改`GenshinMacro.py`中的`game_path`为游戏本体`YuanShen.exe`
路径，脚本会自动启动游戏，如果不想让游戏自动运行，请修改`GenshinMacro.py`
中的`launch_game = True`为`False`。

## 功能

以下内容中`x1`表示靠近手腕的侧键，`x2`表示远离手腕的侧键。

数字键切换角色后自动识别。

联机模式请按住`x2`再点击数字键1~4， 比如四人联机就按住`x2`再按4。

### 通用

- 按住`x2`为循环点击`F`键，可用于自动交互和对话。
- 点击`x1`为自动登龙，目前仅支持作者box中的`单手剑` `双手剑`和`长柄武器`角色和`鹿野院平藏`
  ，其他角色请参考[注意事项](#注意事项)自行调试。
  > [特殊角色](#特殊角色)不支持通用登龙

  > 登龙只适用于60帧及以下，更高帧率请自行修改`character.json`中的延时，帧率越高延时需要越小

### 特殊角色

- **甘雨**
    - 按住`x1`自动蓄力释放`霜华矢`
    - 点击`x2`切换模式
        1. 普通的`霜华矢`蓄力释放
        2. `霜华矢`蓄力释放后闪避
        3. 连续释放两次`霜华矢`后闪避
- **胡桃**
    - 按住`x1`自动AAZ循环
    - 点击`x2`切换模式
        1. 0命循环(AAZ跳)
        2. 1命循环(AAZ闪避)
      > 作者没有1命胡桃，请自行测试修改`Macro.py`中的`胡桃`
- **那维莱特**
    - 按住`x1`自动手法拉满(需自行按攻击键)。
      ![开转](/assets/img/开转！.jpg)

## 注意事项

- 自动登龙延时可能需要根据情况微调，延时为0代表不登龙：
    1. 直接修改`character.json`，单位为毫秒。
    2. 也可修改`GenshinMacro.py`中的`debug = True`和`port`
       ，使用[tcp调试工具](https://play.google.com/store/apps/details?id=com.hardcodedjoy.tcpclient&hl=en_US&pli=1)
       连接调整延时，消息格式为`<延时(毫秒)>s`
       ，消息接收后自动保存。
- 该脚本需要有鼠标侧键，如果没有鼠标侧键请自行修改`Callback.py`。
- 游戏分辨率需设置为`16:10`或`16:9`，否则会报错。
- 该脚本基于图像识别，可能会存在识别错误的情况导致偶尔失灵，不影响使用。
- 推荐使用罗技鼠标并在`GHUB`中恢复侧键的默认设置（如果没有设置过侧键功能请无视），其他鼠标没测试过，不保证能用。
