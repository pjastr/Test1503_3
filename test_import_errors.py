import os, sys, json
import os
import collections

print("This statement is before some imports")

import math
import re

import socket
import hashlib
import csv

from os.path import *

import json


class MyClass:
    def method_one(self):
        return 1

    def method_two(self):
        return 2

    class InnerClass:
        pass


def first_function():
    return "first"


def second_function():
    return "second"


def third_function():
    used_os = os.getcwd()
    used_sys = sys.version
    used_math = math.pi
    used_re = re.compile(r"\d+")
    used_collections = collections.OrderedDict()
    return used_os, used_sys, used_math, used_re, used_collections
