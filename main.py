#!/usr/bin/python
# -*- coding: utf-8 -*-

import fontTools.ttLib.tables
import fontTools.ttLib

s1 = u"今日も一日がんばるぞい！"
s2 = u"死にたい。もう辞めてやる"

tt = fontTools.ttLib.TTFont("mplus-2p-regular.ttf")

chars = set()
glyphMap = dict()
hmtxMap = dict()
for i in range(len(s1)):
    c1 = "uni%04X" % ord(s1[i])
    c2 = "uni%04X" % ord(s2[i])
    chars.add(c2);
    print("{} -> {}".format(c1,c2))
    glyphMap[c2] = tt['glyf'].glyphs[c1]
    hmtxMap[c2] = tt['hmtx'].metrics[c1]
glyphMap['.notdef'] = tt['glyf'].glyphs['.notdef']

for g in dict(tt['glyf'].glyphs):
    if g in chars:
        tt['glyf'].glyphs[g] = glyphMap[g]
        tt['hmtx'].metrics[g] = hmtxMap[g]
    else:
        tt['glyf'].glyphs[g] = fontTools.ttLib.tables._g_l_y_f.Glyph()

output_path = "output.ttf"
tt.save(output_path)
print("wrote {}".format(output_path))
