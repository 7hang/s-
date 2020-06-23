#!/usr/bin/ python
# -*- coding: utf8 -*-
import base64
fp1 = open('users.data','r')
fp2 = open('users.data2','w')
str1 = fp1.readlines()
for line in str1:
    str2 = base64.b64decode(line)
    fp2.write(str2)
fp1.close()
fp2.close()
