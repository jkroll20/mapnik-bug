#!/usr/bin/python
# -*- coding:utf-8 -*-

testxml="""<Map font-directory="." background-color="#ffffff">
<Parameters>
    <Parameter name="bounds">0,0,5,98</Parameter>
</Parameters>
<FontSet name="fontset-1">
    <Font face-name="Noto Sans Hebrew Regular"/>
    <Font face-name="Noto Sans SC Regular"/>
    <Font face-name="Noto Sans TC Regular"/>
    <Font face-name="Noto Sans Regular"/>
</FontSet>
<Style name="text">
    <Rule>
        <TextSymbolizer size="20" fontset-name="fontset-1" clip="false"><![CDATA[[name]]]></TextSymbolizer>
    </Rule>
</Style>
<Layer name="text" srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs">
    <StyleName>text</StyleName>
    <Datasource>
        <Parameter name="type">csv</Parameter>
        <Parameter name="inline">
            x,y,name
%s
            1,3,א
            1,2,א Abc
            1,1,א 汉语
        </Parameter>
    </Datasource>
</Layer>
</Map>"""
aleph_foo="            1,%s,א%c"


if __name__ == '__main__':
    with open("test.xml", "w") as f:
        testfoo= []
        y= 4
        for i in range(127, 0x21, -1):
            testfoo.append(aleph_foo % (y, ('?' if chr(i) in '\'",;<' else i)))
            y+= 1
        f.write(testxml % '\n'.join(testfoo))