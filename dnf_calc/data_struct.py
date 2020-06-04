#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File   : data_struct
# Date   : 2020/5/19 0019
# Author : Chen Ji
# Email  : fzls.zju@gmail.com
# -------------------------------

###########################################################
#                       辅助的数据结构                     #
###########################################################

# 用于实现排行的最小堆
from heapq import heapify, heappush, heappushpop
from multiprocessing import Queue
from multiprocessing.managers import ValueProxy

from numpy import ndarray


class MinHeap:
    def __init__(self, top_n):
        self.h = []
        self.length = top_n
        heapify(self.h)

    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)

    def getTop(self):
        return sorted(self.h, reverse=True)


# re: 发放到工作队列中时，使用copy.deep_copy进行一次深拷贝
class CalcStepData:
    def __init__(self):
        # 装备相关数据
        self.items = []
        self.has_baibianguai = False
        self.not_select_items = []
        self.has_uniforms = []
        self.can_upgrade_work_unifrom_nums = 0
        self.work_uniforms_items = []
        self.transfer_max_count = 0
        self.transfer_slots_equips = []

        # 预计算的一些量
        self.has_god_since = []

        # 计算过程维护的一些中间量
        self.current_index = 0
        self.has_god = False
        # 统计当前最优词条数 re: 这个改为每个工作进程中单独维护，这样尽量避免全局，同时改为普通的整数类型
        self.local_max_setop = 0
        self.max_setopt = 0  # type: ValueProxy[int]
        self.max_possiable_setopt = 3 + 2 + 2 + (1 - 0)  # 533 以及神话对应的一个词条（默认神话优先）
        self.calc_data = CalcData()

        # 一些配置
        self.dont_pruning = False
        self.set_perfect = 0
        self.prefer_god = True
        self.start_parallel_computing_at_depth_n = 0

        # 其他
        self.producer = None
        self.process_func = None


class CalcData:
    def __init__(self):
        # 搜索得到的装备搭配信息
        self.selected_combination = []
        self.baibianguai = None
        self.upgrade_work_uniforms = []
        self.transfered_equips = []

        # 玩家选定的武器
        self.weapon_indexs = []
        # 各种加成
        self.base_array_with_deal_bonus_attributes = []  # type: ndarray
        # 配置表得到的信息
        self.opt_one = {}
        self.job_lv1 = 0
        self.job_lv2 = 0
        self.job_lv3 = 0
        self.job_lv4 = 0
        self.job_lv5 = 0
        self.job_lv6 = 0
        self.job_pas0 = 0
        self.job_pas1 = 0
        self.job_pas2 = 0
        self.job_pas3 = 0
        # 玩家设定的其他信息
        self.cool_on = 0
        self.ele_skill = 0

        # 回传结果的队列
        self.minheap_queue = None  # type: Queue
        # 用于判定是否提前停止计算的变量 re: 这个等下测试性能时先干掉，然后后面通过消息、事件之类的实现。比如calc开始时通知各个工作线程进入工作状态，stop或计算完成时通知各个工作线程进行停止状态
        self.exit_calc = 0  # type: ValueProxy[int]

