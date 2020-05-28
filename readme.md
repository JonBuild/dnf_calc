# 前言
本计算器基于[韩服dawnclass-黎明工作室](https://github.com/dawnclass/DF_Calculator) 所写计算器v2.3.1、[韩械](https://space.bilibili.com/4952736) 汉化并加入国服特色的一键史诗搭配计算器，在其上进行了一些性能优化、扩展功能、易用性改动及bugfix。

目前实现了搜索百变怪、升级工作服、跨界、多武器搭配等功能，并对启动和搜索性能做了一定优化，在操作易用性上加了一些调整。具体改动内容可见下文

# 韩服黎明工作室原版v2.4.0（更新于2020/4/27)
## 原作者github项目地址
https://github.com/dawnclass/DF_Calculator
## 源码发布
https://blog.naver.com/PostView.nhn?blogId=dawnclass16&logNo=221931875095#
## 二进制发布
https://drive.google.com/file/d/1p8ZdzW_NzGKHHOtfPTuZSr1YgSEVtYCj/view

# 网盘链接（更新于2020/5/13)
链接: https://fzls.lanzous.com/s/dnf-calc 提取码: fzls

# 使用简介
## 第一批功能说明
![第一批功能说明](使用说明/功能说明1.png)

## 第二批功能说明
![第二批功能说明](使用说明/功能说明2.png)

## 第三批功能说明
![第三批功能说明](使用说明/功能说明3.png)

# v3.5.8 2020.5.28
## 易用性
1. 某些异常改用Exception，避免遗漏一些未捕捉的异常信息 2. 调用notify_error后要么return，要么exit，需要停止对应代码执行流程

## ui
1. 调整界面装备位置，使套装内顺序与游戏中一致，同时支持通过配置自行调整套装内装备顺序

## bugfix
1. 修复一键点亮如果已经点亮的会被取消的问题

## 增加配置
1. 奶系额外被动等级改为可配置

## 文档支持
1. 更新文档
2. 将首层目录的一些说明也复制到使用说明目录中，同时发布时复制一份各个提示文件到使用说明目录

## 其他
1. readme增加原作者github项目地址信息
2. 蓝奏云试用两周多，可靠性还不错，readme中改为只保留一个更加方便记忆的链接

## 备注
1. 这两天在折腾群聊机器人<_<暂时没空对计算器做一些改动

# v3.5.7 2020.5.26
## ui优化
1. 增加一键全部点亮的功能
2. 初始化默认设置武器为该职业可选择的首个武器

## 增加配置
1. ui字体、背景色改为可配置

## bugfix
3. 计算装备收集数，过滤掉100传说、普雷首饰、普雷特殊装备

# v3.5.6 2020.5.26
## bugfix
1. 展示结果的时候增加判断是否没有结果，以避免刚开始计算还未得到任何结果前就点了停止，导致后续报错
2. 修正读取配置表时没有正确打印出具体错误信息的问题

## 配置逻辑
1. 增加配置检查，当配置有问题时，提示相应错误信息，不允许启动

## 增加词条
1. 增加心悦光环：星空射手的词条：所有职业Lv20~30全部技能Lv+X（特性技能除外）以及用于换装buff时的效果

## ui优化
1. 当套装中只缺某部位普通装备，但对应部位的该套装神话装备已拥有，则同样视为已收集齐该套装
2, 一件点亮套装功能增加支持智慧的产物
3. 智慧的产物收集全和非全的情况下展示不同的图片（规则同其他套装一样）

## 教程
1. 教程中增加其他版本python的下载步骤与截图


# v3.5.5 2020.5.25
## 声明
1. 魔改纯粹出于个人兴趣，如果觉得魔改的东西不符合你的喜好，大可不用，不必特地来阴阳怪气一句：做了xxxx就算个更新了嘛。这只是业余爱好，
    你我之间也没有任何劳务关系，所以也没有理由对我想改什么来进行指责。

## ui优化
1. 神话装备播放gif动画
2. 增加播放gif的配置，可自行设置是否开启，以及播放帧率

## 代码重构
1. 限制全局直接运行的代码仅在ui主线程中执行，为后续多线程改进做准备
2. 将原先各个套装、装备图标的拼接代码改用循环实现，使代码更清晰

# v3.5.4 2020.5.24
## 易用性调整
1. 武器选择列表将只会出现当前职业能够穿戴的武器

# v3.5.3 2020.5.24
## bugfix
1. 修正奶系五个百分比词条实际未生效的问题，在开始计算前需要正确赋值
2. 修正奶系五个百分比词条在计算特色属性时采用了加算的bug，实际应为乘算
3. 各个词条属性类型设为浮点数，避免小数被干掉

## 其他
1. 读取配置文件出错时，需要展示具体错误原因

## ui
1. 结果界面增加版本号

# v3.5.2 2020.5.22
## 针对无法使用打包exe
0. 增加手动安装运行环境的word教程
1. 一键安装脚本默认python版本改为3.5.4，支持更多版本的windows
2. 增加一键关联python脚本
3. 一键安装脚本中pip设置源为国内镜像
4. 一键安装脚本不缓存pip

## 问题反馈
1. 增加问题反馈QQ群的图片，大家有任何使用上的问题，可加QQ群597213951进行反馈

## 版本向前兼容
1. type hints 改用注释的方式，避免旧版本python无法编译
2. 增加一个python35版本的打包脚本-。-
3. requirements.txt中不设置指定版本，默认使用最新版本
4. 增加兼容旧版1-50+1技能词条：extra_all_job_all_level_1_50_skill

## 代码重构
1. 拆分逻辑相关函数
2. 拆分硬件信息相关函数

# v3.5.1 2020.5.21
## 易用性
1. 改写config，改用类实现，从而可以设置默认值，这样在新增配置时，即使使用旧版本的配置文件，也能兼容

## 配置改动
1. 增加日志等级配置

## 调试工具
1. 优化bugsnag上报时附带的上下文信息

# v3.5.0 2020.5.20
## 多线程并发计算支持
1. 使用threading模块实现单核多线程并发计算，最多可完全占用一个逻辑cpu核心，速度大概可以提升一倍
2. 目前在开发使用multiprocessing来实现多核多进程并发，最可可完全占用所有逻辑cpu核心，预期速度可以大幅提升
    2.1 目前的代码结构太过混乱，无法像threading模块一样无痛接入，目前使用multiprocessing创建工作进程时由于与ui主线程在同一线程调用，
        会导致再弹出一个ui，不符合预期，此外很多脚本代码默认全局执行，没有限定在主线程中，导致目前不能直接接入
    2.2 因此目前需要先进行一版代码重构，先将各个模块移到不同的文件中，同时限定其调用行为，部分代码，如logging、config、setting、ui等
        仅限定在主线程中初始化一次

## 数据与韩服原版2.4.9版本同步
1. 男鬼剑更新为三觉数据
2. 之前版本的男格斗的数据就是三觉的数据了，在这里直接列出三觉的，不知道这个数据自己该怎么测。如果有玩男格斗的可以测出对应系数，欢迎在github、贴吧、colg、邮件联系我，更新男格斗二觉的系数（目前仍沿用三觉的数据）
3. 将韩服男枪手三觉的数据同步过来，增加对应条目
4. 更新其他职业的数据到2.4.9版本

ps：本人不知如何计算对应的系数（指这四个被动和六个主动技能在20s和60s下的系数），有会计算的并确认对应结果没啥没问题的欢迎联系我进行更新。

## bugfix
1. 修复读取空行的问题

## 数据表格式调整
1. 美化lvl表格式
2. 装备表增加分隔栏，调整中文字体为微软雅黑
3. 其他表格式美化

## ui美化
1. 字体改为微软雅黑
2. 全部窗口改为可配置为缩放

## 系统参数
1. 增加支持各存档使用不同的打桩系数，若未配置则使用默认的系数，详情请在config.toml中搜索20s_damage.save_name_configs

## 代码重构
1. 将版本、日志、bugsnag、通用报错框放到类库中，并分布到不同文件中，为进一步重构代码结构做准备
2. 提取性能排查工具函数到单独的文件
3. 将最小堆移到单独的文件
4. 抽取ui组件
5. 提取config/setting到单独的文件
6. 将常量提取到单独的文件中
7. TO BE CONTINUED...

## 其他
1. 改变debug.py为run_env.py，用于区分开发环境和发布环境，调整一些应用行为，如在开发环境默认不上报bugsnag，同时对calc不进行try except保护，
    方便调试，发现问题
2. 更新工具子模块版本号
3. 更新ignore文件
4. 更新依赖库版本
5. 打印最终加成的特色词条时，跳过没有实际加成的特色词条

# v3.4.15 2020.5.18
## 排行界面
1. 奶系职业增加一个排行标准：根据祝福适用面板数值
2. 调整一些排行展示界面的代码

## bugfix
1. 抽取分数需要与启用20s伤害配置对应
2. 修正之前发布的debug.py中设为了true的问题，改为另增一个文件，在发布时覆盖，确保发布时未启用调试模式
3. 修正快速模式时若某件套装只有一件神话装备，一件其他装备，此时这个其他装备会被当做散件干掉，不应该这样，修正一下

## 代码重构
1. 原有的一些使用1/2/3三个变量来表示列表的写法改为用列表改写，更加清楚
2. 去除一些因不判断实际排行数目而使用的try except，使得出现异常问题更容易上报
3. 修改一些变量名的名称，使其更加容易理解

## 易用性
1. 可配置是否在点击读取存档按钮时将结果界面干掉
2. 计算完所有特色加成时，在日志中打印出最终加成的总数

## 测试
1. 增加用于测试的测试集，方便做出大量改动时可以快速测试

## 配置改动
1. 将最大存档数改为config配置项
2. 增加说明哪些配置需要重启生效，哪些重载后立即生效

## 其他
1. 增加打开github项目页面的按钮
2. debug.py在仓库中默认设为调试模式，在发布时替换为非调试模式的脚本

# v3.4.14 2020.5.17
## 使用说明
1. 根据bugsnag上报的一些异常，增加相应更加友好的提示，让用户可以知道该怎么改为正确的

# v3.4.13 2020.5.17
## 使用说明
1. 增加bugsnag上报一些不在预期内的错误，方便即时排查问题

# v3.4.12 2020.5.16
## 使用说明
1. 增加各个功能和配置方式的使用说明，并在主界面增加使用说明按钮（替换原有的选择速度提示按钮）
2. 按照@qq273212324建议，将change_log_images改为中文，这样大家都会点进去看一看- -

## 切换蓝奏云
1. 增加一个自定义的更加方便阅读的蓝奏云分享链接

## 易用性
1. 数据表对非0单元格设置特殊颜色，方便查看

## 数据修正
1. @Nirvana_Ch 铁匠鞋子，不加启示圣歌

# v3.4.11 2020.5.13
## 切换蓝奏云
1. 百度网盘频繁抽风，可靠性极差，现决定改用蓝奏云。

# v3.4.10 2020.5.13
## 易用性改动
1. 增加一个fallback处理，当所有网盘链接都失效的时候，引导用户前往github发布页面下载新版本

# v3.4.9 2020.5.13
## 易用性改动
1. 检查更新时，从动态获取的多个网盘分享链接中随机挑选一个未被屏蔽的（若有）作为最终更新链接，增加可靠性<_<

# v3.4.8 2020.5.13
## 新增功能
1. 应@王八老二 需求，在导出奶系职业的排行时，额外导出该组合的三个标准的得分，方便对比

## 新增脚本
1. 增加一键安装python并打包的脚本，方便不能运行我打包的版本，但仍想使用本魔改版本的朋友自行本地打包运行

# v3.4.7 2020.5.13
## 易用性改动
1. 增加检查是否最新的网盘链接失效了，若是则弹窗提醒等待俺去更新网盘链接<_<，避免一脸懵逼-。-

# v3.4.6 2020.5.13
## bugfix
1. 之前版本的限制buff等级上限的实现有bug，若有多个不同的基础等级时，预先处理的等级会有问题，改为在实际计算时截断

# v3.4.5 2020.5.13
## 数据修正
1. 原先奶系职业的普雷特殊和首饰实际为100传说装备的属性，统一调为普雷（太阳）
2. 原先输出的职业的普雷装备均为太阳，增加标记

ps：处于时间因素，只将原装备改为普雷太阳，如果希望添加大地与天空，可自行添加139（大地首饰）、140（大地特殊）、141（天空首饰）、142（天空特殊），
    并将image文件夹中137（太阳首饰）、138（太阳特殊）的6张装备图片复制两份，分别改为139/140/141/142，并在data.xlsx的one 和 buf sheet中分别添加这12件装备的属性
    （三件套的属性直接赋值137/138的即可（改名为对应套装名）。思路很清晰，就是感觉没必要也没时间做这个- -谁需要的话就自己按照这个步骤加一下，预计半小时到一个小时左右能搞定。
    此外还得在脚本中get_equips函数中在原来添加普雷装备的地方把这些也给加上


# v3.4.4 2020.5.12
## 网盘更新
1. 网盘链接炸了，修改readme中的网盘地址链接
2. 调整自动更新时的网盘链接地址获取方式，改为从github主页实时获取，避免日后网盘链接再次炸掉

## 数据调整
1. 调整奶爸初始体精
2. 将奶系职业的面板转换等级系数和唱歌倍率的系数改为可配置项

## 其他
1. 换版本提示额外增加自定义特色配置文件

## 开发工具
1. 发布脚本增加输入版本号的功能

# v3.4.3 2020.5.11
## 增加词条
1. 增加两个换装用的词条，只增加祝福等级，不加其他的

## bugfix
1. 护石配置的技攻没有按百分比来算，重新调整一下
2. 奶的buff等级上限处理，否则当buff超过上限时，去对应数值时会抛异常

## 其他改动
1. 如果计算过程出现了未处理的异常，则写错误日志，并弹出错误框，显示对应traceback信息

# v3.4.2 2020.5.11
## bugfix
1. 解决因特色加成的额外技攻没有在计算时赋值到skiper中而导致该特色未生效的问题

# v3.4.1 2020.5.11
## 易用性改动
1. 配置文件和配置表支持动态加载

## 数据配置
1. 其他特色可以配置公共的特色，如冒险团和公会属性，这样就不用每个角色都重复配置一遍了
2. 奶系职业的初始体精和智力改用config.toml进行配置

## 其他改动
1. 使用logging模块来进行日志输出，方便排查错误
2. <_<增加恰饭图片哈哈哈哈哈哈

# v3.4 2020.5.10
## 前言
本版本的数据改动较大，如果要使用，建议按照下面的操作将自定义属性中相关数值清空，并在setting/account_other_bonus_attributes.yaml中
按照示例增加对应角色的实际国服特色属性。如果不填的话，这个版本会无法使用（完全不准，因为新版本默认数据表中没有附加的国服特色，自定义
属性中的国服特色相关配置也都移到对应配置表中了）

## 新版国服特色示例
1. 以本人的奶妈、召唤为示例,添加其他国服特色示例,并增加一些新的特色词条
2. 移除加在武器上面的国服特色
    2.1. 力智+500
    2.2. 三攻+200
    2.3. 攻击时，附加8%的伤害
    2.4. 最终伤害+3%
    2.5. 50级主动+3
3. 干掉自定义属性中的一些属性（现已可通过自定义国服特色来实现）
    3.1 奶量增幅的所有数值可以减为0了
    3.2 属强提升中的技能属强、其他属强、勋章属强也可以干掉了
    3.3. 初始属强改为19
4. 调整奶妈的初始智力


## bugfix
1. 解决奶的buflvl表读取偏移了的问题

## ui优化
1. 处理奶的展示界面中一觉被动部分未汉化的问题
2. 解决当奶系职业展示界面右侧五个搭配中有搭配没有百变怪时，切换到其他标准后，若该位置有百变怪，切回原标准后，这个位置的百变怪仍在那里的问题
3. 尝试在结果界面中增加奶妈奶萝的站街面板（不一定准）
4. 加上一个预估的伤害值（不一定准）
    4.1 如果不想显示预估的打桩数据，可以通过配置取消
    4.2 可自行配置分数与打桩的比例关系，从而更加适应自己的角色的打桩数据（目前暂时认为分数与打桩结果是线性相关的）


# v3.3 2020.5.5
## 重构
1. 重构国服特色的实现方式，实现完全配置驱动。用户可以自行通过修改配置表来实现增减国服特色了。
1.1 将原先写死在脚本中的各个国服特色属性改为使用配置表来填写，具体可见setting目录下的各个配置表
1.1.1 setting/styles.yaml 称号的配置表，若需新增称号，可以自行按照现有示例和表头填写规则自行添加，下次启动时将自动出现在称号列表中
1.1.2 setting/creatures.yaml 宠物的配置表，若需新增宠物，可以自行按照现有示例和表头填写规则自行添加，下次启动时将自动出现在宠物列表中
1.1.3 setting/account_other_bonus_attributes.yaml 其余国服特色的配置表，配置方式与上面俩几乎一致，只是names的含义不再是特色的名称，而是存档的名字。
        程序计算时，会从这里面尝试找到当前存档对应的特色列表，并加成到角色属性中。
        可以参照现有注释，每个存档建立一个条目，然后在该条目的entries下按照各个特色，分别把对应词条加进去，如技能宝珠的1-50技能+1、力智+75这种可以用现有词条来表达
        如果有不能表达的词条，建议在贴吧帖子中告知，我在后续添加支持即可。
1.2 程序侧将特色的各个词条抽象出来，供配置表自行配置。并将其映射为输出职业和奶系职业的各个属性，从而实现特色词条到角色属性的转换。
1.3 实际计算特色加成时，根据特色类别和选用的特色，去配置表中找到对应条目进行应用，若使用python直接运行，会在console中看到实际应用的词条和对应属性
2. 在新版的国服特色架构下，奶系也可以享受到特色加成。

## 添加国服特色
1. 增加弓小弦、甜小鱼心悦宠物

## ui优化
1. 展示概览时，按次数多的在前面，其次套装序号小的在前面的规则排列，保证顺序一致
2. 调整show name 中的顺序，将为了优化神话部位搜索顺序而调整顺序的装备序列改回正常顺序再展示
3. 增加更多国服特色配置的引导按钮
4. 当用户取消更新时弹出提示如何关闭检查更新的方法

## 易用性改动
1. 增加配置项 是否检查更新，默认启用，这样用户可以自行选择是否每次启动时检查更新

## 汉化
1. 将奶系职业装备词条名称改为游戏内显示的词条名
2. 增加奶系职业的下标说明
3. 调整奶系职业计算过程的各种变量的名称，使其更加容易阅读
4. 在sheet1中额外注释buflvl中各个行的含义

## 其他改动
1. 增加打印有哪些特色，生效什么词条，对应职业哪些属性
2. 应韩械要求，将原作者的工作室和博客名放到标题上

# v3.2.9.1 2020.5.3
## bugfix
1. 心悦宠物忘记加到宠物列表中了，虽然实际逻辑分支已经加了= =

# v3.2.9 2020.5.3
## 新增功能
1. 增加可通过配置来启用导出任意个排行结果到excel文件的功能 @撒打算多万 以及另一个找不到了网友建议的增加结果界面的数目（ui太麻烦了，就用这个替代吧）
    新版本中增加了config.toml，其中增加了导出excel相关的配置，默认关闭，如果有需求，可以将enable的值设为true，调整导出名和导出数目，即可体验该功能
2. 增加读取配置功能

## 代码调整
1. 调整查找版本号的正则，使其更健壮

# v3.2.8.3 2020.5.2
## bugfix
1. 阳剑技攻调为59.9=（1.30*1.23)-1
2. 经多名贴吧网友反馈，歧路、不息、裁决者等装备属性异常高。经排查，由于之前保存自定义中调整装备属性时，装备的行号是写死的，导致调整装备顺序、
    位置或新增装备时，可能对应保存地方与预期不一致。改为在启动时预先获取各个装备编码对应的行号，在需要特别定位某个装备时，通过装备编码来获取对应行号。
3. 普雷魔法石与辅助装备的图标反了，@-最皮吧友
4. 修复增加青沙棍后，之后的武器id都增1，但buf表中奶系的武器的id没有调整（仍为111040-111043），导致前三把武器实际数据后后三把，而最后一把则找不到对应数据 @Johnny丶Qian
5. 拥有军神耳环，且不拥有军神辅助装备，需要减去10%力智加成 @本子导致羊尾
6. 调整宠物技能10%增伤的实现，因为是直接乘算最终伤害的，又因为一般队友也有，所以一般能全程迟到，所以改为当做10%技攻

## ui优化
1. 调整各个窗口的大小与位置 @Nirvana_Ch
2. 对齐和优化自定义界面 @Nirvana_Ch
3. 大恍惚增幅范围改为0-13 @Nirvana_Ch
4. 调整存档数为100个，并调整额外存档数据的存盘区域以适应新的存档数目，同时增加对旧版存档数据的兼容处理
5. 调整更改存档名的流程，直接在存档名文本框中修改，然后点击存档即可

## 使用便利性
1. 在读档A后，切换其他存档B，然后误点存档并确认后用存档B把存档A给覆盖这种情况时，额外弹出一个确认框，提示，用户可以自行确定是否真想这么做
2. 启动时增加检查更新功能，若有更新会提示是否更新，确认后会弹出网盘页面，并弹窗告知提取码

## 其他改动
1. 调整主窗口标题
2. 特殊成套装备在不成套时减掉属性的处理加上注释
3. 增加心悦宠物 @老贺最

# v3.2.8.2 2020.4.30
## bugfix
1. 经贴吧网友@王八老二 反馈，魔改后版本的神话装备图片没有原来那么闪，并给出了对比图，经排查发现作者在images目录中神话装备会有三个文件，
    分别是以n.gif/n.png/f.png结尾，对应超闪耀，点亮、暗淡三种，实际上原版神话装备只用了1和3，但是优化加载图片时是改为文件夹中有多少个图片就按需加载，
    由于前俩的key都是装备编码，而且超闪亮的是先加载的，所以会被普通闪给覆盖。目前已修复
2. 经贴吧多名网友反馈，奶系职业无法使用也与黑瞳武器，经排查发现原版数据表中夜语黑瞳武器为111001，韩械魔改后为111014，而没在buf表中同步，已修复
3. 经贴吧网友@阿飘 反馈，太极天帝剑（阳）攻速不对，应为-50%，实际写成了20%，同时修复了顺带发现的太极天帝剑技能攻击力不对的问题，应为53%（30+23），而不是60%
    3.1 经贴吧网友@划圆为牢 反馈，天帝剑的技攻是乘算的，1.30*1.23=1.599 约等于60技攻的提升，改回去= =
4. 百变怪不能转化为传说、普雷
5. 多名网友反馈希望不要默认将普雷传说加入备选池，考虑到两种方案都有一定需求，增加配置项：是否默认将普雷传说装备加入备选池
6. 经贴吧网友@～Smile 反馈，增加不优先神话的中速方案，选择该方案时，神话装备与普通装备具有相同的优先级

## 数据改动
1. 应多位贴吧网友要求，增加了2019升级版至尊年宠 '神迹·古国英豪莱恩', '神迹·太初之音薇泽达'
2. 经贴吧网友建议，将宠物技能的3.3%期望伤害改为最终伤害，因为这个技能是直接最后加成上去的
3. 为了方便日后改动，借助谷歌翻译和对照游戏内的装备数据，在上周汉化Data.xlsx中one sheet的基础上将全部表格汉化了

## 易用性改动
1. 调整武器顺序，将顺序改为韩服作者原先的顺序，方便大家找武器
2. 发现原版中的青沙棍在韩械增加普雷武器时被替换成普雷武器了，现已加回来
3. 按照游戏中冒险团页面角色收藏簿的顺序重新排列职业，方便查找，并将奶妈、奶萝、奶爸改回原来的名字并放到对应位置（强迫症），将其他角色的名称调成与游戏中一致，如男女鬼剑，铁血统帅，并在读取存档时针对职业名称变化，增加兼容处理

## 其他改动
1. 加入百度网盘的地址，方便大家查找下载二进制
2. 增加韩服4.27发布的最新版2.4.0源码与相关发布页面，并在readme文件中增加韩服原作者与韩械的链接

# v3.2.8.1 2020.4.26
## bugfix:
1. 经贴吧网友@反正有大好时光 @Usingaa @丿俊哥丶，新版本中自定义功能出现问题，经排查定位到是因为多增加了一行列名含义后，保存自定义结构的代码中写死的坐标会找到错误的定位，已修复
2. 经贴吧网友@罗衣 @git，奶系选择百变怪后计算有时候会卡住，经排查发现是因为写法与输出那边不太一样，导致相同的处理办法直接拷贝过来会有问题，已修复
3. 发现新加的套装概览区域不会随查看详细信息和更改奶量标准变动，查了下，发现是做的时候太忙了，忘记了。。。已修复

## 开发工具
1. 新增脚本_export_excel_to_txt.py，用于将data.xlsx与preset.xlsx导出为文本格式，方便进行版本对比，避免误改动到数据文件

# v3.2.8 2020.4.26
## 新增功能
1. 增加装备跨界功能，因计数部分太复杂，不再维护
2. 增加选择多个武器的功能，因计数部分太复杂，不再维护
3. 增加区域展示更加方便阅读的当前搭配，如天擎3水果2这种
4. 结果栏中增加查看名称按钮，点击即可查看当前搭配的各部位装备名称，不用再看图认出装备了
5. 增加当前用时，方便看花了多少时间了
6. 在显示当前组合数的地方，在前面加上装备的收集进度
7. 把结果界面的层级不设置最顶端，这样出结果后切换其他角色时不需要额外折腾
8. 增加多选列表组件
9. 增加与贝奇邂逅称号（因为我的奶妈在用这个<_<)
10. 汉化data.xlsx
11. Data.xlsx增加首行，表示各列的中文含义，同时冻结第一行与前两列，这样编辑具体数值时容易定位

## bugfix
1. 根据b站网友@面粉馅包子 的反馈，之前版本的百变怪功能在特定装备级下，百变怪没有选择最合适的转换装备。
    经排查发现，是因为作者根据搭配套装数目预估价值量的函数f=sum([floor(x * 0.7) for x in set_val.values()]) + god,
    与其实际精确搭配的奶量伤害的函数g，不能满足在任意区间内都具有相同的函数单调性（递增或递减），
    从而可能或出现对于某些搭配x1,x2，f（x1）<f(x2)，而g(x1)>g（x2），在作者的原剪枝流程中，会导致x1搭配被视为无效搭配。

    解决办法：
    1. （非常耗时）计算每个搭配的精确伤害奶量来找到在该伤害奶量算法下的精确解
    2. （实现难度高）找到更合适的价值评估函数，在满足与该伤害奶量算法相同增减性的同时，且计算代价小
    3. （自行选择精确度还是速度）仍使用当前算法，忍受为了计算速度而可能错过一些精确解的bug，
        与此同时，增加超慢速选项，允许用户选择使用花费更多时间来得到更精确的解。
        但是这种情况下，由于无法进行提前剪枝，需要计算所有组合，其时间复杂度将是O(n1*n2*...n10*n11)，
        其中ni为部位i的可选装备数目，在各部位都有一定数目的情况下，用时将难以想象

    出于个人精力有限，目前暂时选择方案3，在速度选项再增加一个超慢速方案，当选择该方案时，所有剪枝与预判都会停用，对比装备的唯一标准
    就是作者实际计算伤害奶量的算法结果

    排查过程截图详见网盘或贴吧帖子
2. 经韩械反馈，属强多出来了80点，应该是之前他在data.xlsx中补正的数值我这边重新计算了一遍- -，暂时先在国服特色的函数中减去一定数值，保证两边属强计算结果一样
3. 经贴吧网友@飞花逐月反馈，在五个散件防具、两首饰、两特殊这种类似的情况下，原版只会给出唯一的史诗组成的搭配，而略过了实际战力更高的传说普雷搭配。
   为了计算结果更精确，永远将100传说防具、普雷首饰、普雷特殊加入备选方案
4. 经贴吧网友@萌萌的汉堡包反馈，在特定组合下选择百变怪计算奶量时程序会无法计算，提示时间很长，经排查，是之前遇到过的一个bug，只是修复了输出职业的那边，奶这边没有改。
   具体原因：目前select是默认初始化时将tg{1101-3336}[0,1]范围的key对应的值都设为0，而百变怪会根据select的值为0来筛选出未选择的集合，
   因此在获取装备属性切片时，如果因为这件装备时间不存在，导致切片为None而空指针访问程序无法正常执行。这种情况，直接判断空指针返回就可以了


# v3.2.7.2 2020.4.23
1. 经韩械反馈，原先版本已经实现了至尊宠物所带来的5%最终伤害，一级1-50级技能+1，只不过实现方式是在Data.xlsx中所有武器的这两个属性中分别加了相应值，
    因此，3.2.7版本的最终伤害会高5%，1-50级技能等级会多出1点来
    根据他的建议，目前从Data.xlsx中移除了这两个加成，并在那边的另一个1-50级技能+1（暂不明确来源）加到国服特色的代码中

# v3.2.7.1 2020.4.23
1. 经贴吧吧友@给QQ一巴掌 提示，发现在调整国服特色数值实现的过程中，把原有的初始属强给漏了，这里给补回来

# v3.2.7 2020.4.21
1. 增加支持更多春节宠物、称号和国庆称号，并尽可能将每个词条都考虑进来
2. 修复夜语黑瞳武器55技攻变成55速度的问题
3. 修复update_count和update_count2在tkinter.mainloop启动前就调用tkinter相关组件而导致计算倒计时的功能挂掉的bug
4. 增加每个词条的枚举，而不是使用magic number来访问- -
5. 汉化data中的部分装备名称

# v3.2.6 2020.4.20
1. 百变怪的备选集合中排除升级得到的工作服、智慧产物
2. 新增可配置最多升级n件工作服的功能
3. 目前select是默认初始化时将tg{1101-3336}[0,1]范围的key对应的值都设为0，而百变怪会根据select的值为0来筛选出未选择的集合，因此在这里如果为None，将其过滤掉，避免程序不运行
    3.1 bug来源：@我就水亿贴 贴吧网友的反馈
4. ui细节调整
5. 增加推荐使用步骤及免责声明
6. 增加一件发布脚本
7. 增加加入升级工作服功能后，剪枝时的精确计数，后因性能问题回滚


# v3.2.5 2020.4.20
1. 修复奶系职业切换排序标准时右侧搭配不刷新的问题
2. 输出结果界面额外汉化
3. 输出界面排版优化

# v3.2.4 2020.4.19
1. 将保存结果的结构体由列表改为最小堆（存储O(n)，排行O(1)），原先的排行消耗太大(存储O(n*logn),排行O(n^2))，尤其是在点亮全部装备的时候尤为显著

# v3.2.3 2019.4.19
1. 修复状态栏中剪枝时未计入后续组合中的百变怪的组合而导致算的增加的无效组合数低于实际剪枝数目
2. 修复下方统计总数时因将神话装备算入百变怪备选集合而导致总数与上方计得数字不一致的问题
3. 添加无提前剪枝和最宽泛上限的剪枝方案
3.1 测试数据无提前剪枝用时123s
3.2 测试数据最宽泛上限剪枝用时9s
3.2.1 每个剩余装备按1点增益计算，若目前序列尚无神话，且后续序列存在神话，则额外加一点
3.2 测试数据任意现有装备下新增若干个装备剪枝用时8.99s
3.2.2 当前已有装备不受限制，预先计算任意新增k个装备所能得到的最大增益，若目前序列尚无神话，且后续序列存在神话，则额外加一点

# v3.2.2 2019.4.19
由于下周或者下下周，基本上大部分人的百变怪都做出来了，那时候大家可能会烦恼如何使用计算器来看这个百变怪该选啥，为了不至于一个个去尝试，因此增加了下述功能
1. 将itertools.product改为自行实现，方便在中间过程进行剪枝
2. 增加百变怪功能，当选择拥有百变怪选项时，计算搭配时会将百变怪考虑进来

# v3.2.1 2019.4.14
1. 存档读档功能增加支持选择速度、武器、职业选择、输出时间、称号选择、宠物选择、冷却补正等信息，无需每次读档后再手动设定后才能进行计算，现在读档后可以直接点计算
2. 启动时自动读取首个存档，无需再自己去点一次读档才能去进行其余操作
3. 性能优化：
    3.1. 调整读取装备图片的流程，通过遍历文件夹来实现加载所需的图片，而不是穷举所有可能，最后导致启动时要卡顿两秒，根据测试，目前读取图片共使用0:00:01.780298秒, 总共尝试加载6749个， 有效的加载为351个
    3.2. 国内环境无法访问他那个更新版本的google网盘地址，所以直接移除相关代码
4. 干掉了在总组合数目超过5亿种时不允许玩家运行的限制，同时将遍历组合的流程由先生产所有改为使用生成器去遍历，使得在组合数非常大时内存也不会溢出，经测试即时点亮所有图标，新版本也能够正常计算
5. 增加计算预计剩余时间的功能，在计算栏中将初始化右侧已显示的当前总组合数移除，改为预计剩余计算时间，这样可以更容易知道进度
6. 初始状态设为停止状态，在成功开始计算时设为计算状态，结束计算时和按停止时设为停止状态
7. 保证职业列表按照excel表中的行顺序排列
8. 未选择职业或武器直接点计算时弹出错误框，使得更加易用
