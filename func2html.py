import base64
import requests
import json
import os
import codecs
import re
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(BASE_DIR, 'Middle')
GRADE1 = os.path.join(CODE_DIR, 'Grade1')
GRADE2 = os.path.join(CODE_DIR, 'Grade2')
GRADE3 = os.path.join(CODE_DIR, 'Grade3')

P1 = "두"
P2 = "LEFT"
P3 = "다음"
P4 = "어느"
LTAG = "$$수식$$"
RTAG = "$$/수식$$"
LTABLE = "$$표$$$$셀$$"
RTABLE = "$$/셀$$$$/표$$"
TDIR = "models/IO/temp/"


front = """<?xml version='1.0' encoding='utf-8'?>
<HWPML Style="embed" SubVersion="8.0.0.0" Version="2.8">
  <HEAD SecCnt="1">
    <DOCSUMMARY>
      <TITLE>이고 수직선에서 </TITLE>
      <AUTHOR>ICL2</AUTHOR>
      <DATE>2019년 6월 5일 수요일 오후 5:46:14</DATE>
    </DOCSUMMARY>
    <DOCSETTING>
      <BEGINNUMBER Endnote="1" Equation="1" Footnote="1" Page="1" Picture="1" Table="1" />
      <CARETPOS List="0" Para="3" Pos="4" />
    </DOCSETTING>
    <MAPPINGTABLE>
      <FACENAMELIST>
        <FONTFACE Count="3" Lang="Hangul">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="Latin">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="Hanja">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="Japanese">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="Other">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="Symbol">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
        <FONTFACE Count="3" Lang="User">
          <FONT Id="0" Name="나눔고딕" Type="ttf">
            <TYPEINFO ArmStyle="0" Contrast="0" FamilyType="2" Letterform="0" Midline="0" Proportion="4" SerifStyle="13" StrokeVariation="0" Weight="6" XHeight="0" />
          </FONT>
          <FONT Id="1" Name="함초롬돋움" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="11" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
          <FONT Id="2" Name="함초롬바탕" Type="ttf">
            <TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" SerifStyle="3" StrokeVariation="1" Weight="6" XHeight="1" />
          </FONT>
        </FONTFACE>
      </FACENAMELIST>
      <BORDERFILLLIST Count="2">
        <BORDERFILL BackSlash="0" BreakCellSeparateLine="0" CenterLine="0" CounterBackSlash="0" CounterSlash="0" CrookedSlash="0" Id="1" Shadow="false" Slash="0" ThreeD="false">
          <LEFTBORDER Color="0" Type="None" Width="0.1mm" />
          <RIGHTBORDER Color="0" Type="None" Width="0.1mm" />
          <TOPBORDER Color="0" Type="None" Width="0.1mm" />
          <BOTTOMBORDER Color="0" Type="None" Width="0.1mm" />
          <DIAGONAL Color="0" Type="Solid" Width="0.1mm" />
        </BORDERFILL>
        <BORDERFILL BackSlash="0" BreakCellSeparateLine="0" CenterLine="0" CounterBackSlash="0" CounterSlash="0" CrookedSlash="0" Id="2" Shadow="false" Slash="0" ThreeD="false">
          <LEFTBORDER Color="0" Type="None" Width="0.1mm" />
          <RIGHTBORDER Color="0" Type="None" Width="0.1mm" />
          <TOPBORDER Color="0" Type="None" Width="0.1mm" />
          <BOTTOMBORDER Color="0" Type="None" Width="0.1mm" />
          <DIAGONAL Color="0" Type="Solid" Width="0.1mm" />
          <FILLBRUSH>
            <WINDOWBRUSH Alpha="0" FaceColor="4294967295" HatchColor="4278190080" HatchStyle="-1" />
          </FILLBRUSH>
        </BORDERFILL>
      </BORDERFILLLIST>
      <CHARSHAPELIST Count="6">
        <CHARSHAPE BorderFillId="2" Height="1000" Id="0" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="2" Hanja="2" Japanese="2" Latin="2" Other="2" Symbol="2" User="2" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
        <CHARSHAPE BorderFillId="2" Height="1000" Id="1" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
        <CHARSHAPE BorderFillId="2" Height="900" Id="2" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
        <CHARSHAPE BorderFillId="2" Height="900" Id="3" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="2" Hanja="2" Japanese="2" Latin="2" Other="2" Symbol="2" User="2" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
        <CHARSHAPE BorderFillId="2" Height="900" Id="4" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="-5" Hanja="-5" Japanese="-5" Latin="-5" Other="-5" Symbol="-5" User="-5" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
        <CHARSHAPE BorderFillId="2" Height="1100" Id="5" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
          <FONTID Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
          <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
          <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        </CHARSHAPE>
      </CHARSHAPELIST>
      <TABDEFLIST Count="2">
        <TABDEF AutoTabLeft="false" AutoTabRight="false" Id="0" />
        <TABDEF AutoTabLeft="true" AutoTabRight="false" Id="1" />
      </TABDEFLIST>
      <NUMBERINGLIST Count="1">
        <NUMBERING Id="1" Start="0">
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="1" NumFormat="Digit" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">^1.</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="2" NumFormat="HangulSyllable" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">^2.</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="3" NumFormat="Digit" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">^3)</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="4" NumFormat="HangulSyllable" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">^4)</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="5" NumFormat="Digit" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">(^5)</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="6" NumFormat="HangulSyllable" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">(^6)</PARAHEAD>
          <PARAHEAD Alignment="Left" AutoIndent="true" CharShape="4294967295" Level="7" NumFormat="CircledDigit" TextOffset="50" TextOffsetType="percent" UseInstWidth="true" WidthAdjust="0">^7</PARAHEAD>
        </NUMBERING>
      </NUMBERINGLIST>
      <PARASHAPELIST Count="12">
        <PARASHAPE Align="Left" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="false" Condense="0" FontLineHeight="false" Heading="0" HeadingType="None" Id="0" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="0" LineSpacing="130" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" Heading="0" HeadingType="None" Id="1" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="-2620" Left="0" LineSpacing="130" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="false" Condense="0" FontLineHeight="false" Heading="0" HeadingType="None" Id="2" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="0" LineSpacing="150" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" Heading="0" HeadingType="None" Id="3" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="4" KeepLines="false" KeepWithNext="false" Level="6" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="14000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="5" KeepLines="false" KeepWithNext="false" Level="5" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="12000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="6" KeepLines="false" KeepWithNext="false" Level="4" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="10000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="7" KeepLines="false" KeepWithNext="false" Level="3" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="8000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="8" KeepLines="false" KeepWithNext="false" Level="2" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="6000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="9" KeepLines="false" KeepWithNext="false" Level="1" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="4000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="20" FontLineHeight="false" Heading="0" HeadingType="Outline" Id="10" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="1" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="2000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
        <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" Heading="0" HeadingType="None" Id="11" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
          <PARAMARGIN Indent="0" Left="3000" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
          <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" OffsetBottom="0" OffsetLeft="0" OffsetRight="0" OffsetTop="0" />
        </PARASHAPE>
      </PARASHAPELIST>
      <STYLELIST Count="14">
        <STYLE CharShape="5" EngName="Normal" Id="0" LangId="1042" Name="바탕글" NextStyle="0" ParaShape="3" Type="Para" />
        <STYLE CharShape="0" EngName="Body" Id="1" LangId="1042" Name="본문" NextStyle="1" ParaShape="11" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 1" Id="2" LangId="1042" Name="개요 1" NextStyle="2" ParaShape="10" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 2" Id="3" LangId="1042" Name="개요 2" NextStyle="3" ParaShape="9" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 3" Id="4" LangId="1042" Name="개요 3" NextStyle="4" ParaShape="8" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 4" Id="5" LangId="1042" Name="개요 4" NextStyle="5" ParaShape="7" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 5" Id="6" LangId="1042" Name="개요 5" NextStyle="6" ParaShape="6" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 6" Id="7" LangId="1042" Name="개요 6" NextStyle="7" ParaShape="5" Type="Para" />
        <STYLE CharShape="0" EngName="Outline 7" Id="8" LangId="1042" Name="개요 7" NextStyle="8" ParaShape="4" Type="Para" />
        <STYLE CharShape="1" EngName="Page Number" Id="9" LangId="1042" Name="쪽 번호" NextStyle="0" ParaShape="0" Type="Char" />
        <STYLE CharShape="2" EngName="Header" Id="10" LangId="1042" Name="머리말" NextStyle="10" ParaShape="2" Type="Para" />
        <STYLE CharShape="3" EngName="Footnote" Id="11" LangId="1042" Name="각주" NextStyle="11" ParaShape="1" Type="Para" />
        <STYLE CharShape="3" EngName="Endnote" Id="12" LangId="1042" Name="미주" NextStyle="12" ParaShape="1" Type="Para" />
        <STYLE CharShape="4" EngName="Memo" Id="13" LangId="1042" Name="메모" NextStyle="13" ParaShape="0" Type="Para" />
      </STYLELIST>
    </MAPPINGTABLE>
    <FORBIDDENSTRING>
      <FORBIDDEN Id="0">IAA=</FORBIDDEN>
      <FORBIDDEN Id="1">IAA=</FORBIDDEN>
      <FORBIDDEN Id="2">IAA=</FORBIDDEN>
      <FORBIDDEN Id="3">IAA=</FORBIDDEN>
    </FORBIDDENSTRING>
  </HEAD>
  <BODY>
    <SECTION Id="0">
      <P ColumnBreak="false" PageBreak="false" ParaShape="3" Style="0">
        <TEXT CharShape="5">
          <SECDEF CharGrid="0" ExtMasterpageCount="0" FirstBorder="false" FirstFill="false" LineGrid="0" OutlineShape="1" SpaceColumns="1134" TabStop="8000" TextDirection="0">
            <STARTNUMBER Equation="0" Figure="0" Page="1" PageStartsOn="Both" Table="0" />
            <HIDE Border="false" EmptyLine="false" Fill="false" Footer="false" Header="false" MasterPage="false" PageNumPos="false" />
            <PAGEDEF GutterType="LeftOnly" Height="84188" Landscape="0" Width="59528">
              <PAGEMARGIN Bottom="4252" Footer="4252" Gutter="0" Header="4252" Left="8504" Right="8504" Top="5668" />
            </PAGEDEF>
            <FOOTNOTESHAPE>
              <AUTONUMFORMAT SuffixChar=")" Superscript="false" Type="Digit" />
              <NOTELINE Color="0" Length="-1" Type="Solid" Width="0.12mm" />
              <NOTESPACING AboveLine="850" BelowLine="567" BetweenNotes="283" />
              <NOTENUMBERING NewNumber="1" Type="Continuous" />
              <NOTEPLACEMENT BeneathText="false" Place="EachColumn" />
            </FOOTNOTESHAPE>
            <ENDNOTESHAPE>
              <AUTONUMFORMAT SuffixChar=")" Superscript="false" Type="Digit" />
              <NOTELINE Color="0" Length="14692344" Type="Solid" Width="0.12mm" />
              <NOTESPACING AboveLine="850" BelowLine="567" BetweenNotes="0" />
              <NOTENUMBERING NewNumber="1" Type="Continuous" />
              <NOTEPLACEMENT BeneathText="false" Place="EndOfDocument" />
            </ENDNOTESHAPE>
            <PAGEBORDERFILL BorderFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Both">
              <PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" />
            </PAGEBORDERFILL>
            <PAGEBORDERFILL BorderFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Even">
              <PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" />
            </PAGEBORDERFILL>
            <PAGEBORDERFILL BorderFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Odd">
              <PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" />
            </PAGEBORDERFILL>
          </SECDEF>
          <COLDEF Count="1" Layout="Left" SameGap="0" SameSize="true" Type="Newspaper" />
          """
end = """    </SECTION>
  </BODY>
</HWPML>
"""
left_char = "<CHAR>"
right_char = "</CHAR>"
left_script = """<EQUATION BaseLine="86" BaseUnit="1200" LineMode="false" TextColor="0" Version="Equation Version 60">
            <SHAPEOBJECT InstId="2119211419" Lock="false" NumberingType="Equation" TextFlow="BothSides" ZOrder="4">
              <SIZE Height="%s" HeightRelTo="Absolute" Protect="false" Width="%s" WidthRelTo="Absolute" />
              <POSITION AffectLSpacing="false" AllowOverlap="false" FlowWithText="true" HoldAnchorAndSO="false" HorzAlign="Left" HorzOffset="0" HorzRelTo="Para" TreatAsChar="true" VertAlign="Top" VertOffset="0" VertRelTo="Para" />
              <OUTSIDEMARGIN Bottom="0" Left="56" Right="56" Top="0" />
            </SHAPEOBJECT>
            <SCRIPT>
            """
right_script = """</SCRIPT>
          </EQUATION>
          """
left_p = """<P ColumnBreak="false" InstId="2147483648" PageBreak="%s" ParaShape="3" Style="0">
        <TEXT CharShape="5">
        """
right_p = """</TEXT>
      </P>
      """

left_table = """<TABLE BorderFill="2" CellSpacing="0" ColCount="1" PageBreak="Cell" RepeatHeader="true" RowCount="1">
            <SHAPEOBJECT InstId="2138179088" Lock="false" NumberingType="Table" TextFlow="BothSides" ZOrder="0">
              <SIZE Height="4882" HeightRelTo="Absolute" Protect="false" Width="41954" WidthRelTo="Absolute" />
              <POSITION AffectLSpacing="false" AllowOverlap="false" FlowWithText="true" HoldAnchorAndSO="false" HorzAlign="Left" HorzOffset="0" HorzRelTo="Para" TreatAsChar="true" VertAlign="Top" VertOffset="0" VertRelTo="Para" />
              <OUTSIDEMARGIN Bottom="283" Left="283" Right="283" Top="283" />
            </SHAPEOBJECT>
            <INSIDEMARGIN Bottom="141" Left="510" Right="510" Top="141" />
            <ROW>
              <CELL BorderFill="2" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="false" Header="false" Height="282" Protect="false" RowAddr="0" RowSpan="1" Width="41954">
                <PARALIST LineWrap="Break" TextDirection="0" VertAlign="Center">
                """

right_table = """</PARALIST>
              </CELL>
            </ROW>
          </TABLE>
          """


SCRIPT_VALUES = ["times", "div", "leq", "geq", "therefore", "because", "deg", "over", "sqrt", "left", "right"]


def load_positions(filename):
    w_dict = {}
    h_dict = {}
    with codecs.open(filename, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            item = line.strip().split("\t")
            if len(item) == 3:
                if item[0].lower() in SCRIPT_VALUES:
                    w_dict[item[0].lower()] = int(item[1])
                    h_dict[item[0].lower()] = int(item[2])
                else:
                    w_dict[item[0]] = int(item[1])
                    h_dict[item[0]] = int(item[2])
    return w_dict, h_dict




def compute_width(script, w_dict):
    script_items = script.split()
   
    position = 300
    nposition = 0
    dposition = 0
    over_flag = False
    wrap_flag = False
    for sitem in script_items:
        if sitem.lower() in SCRIPT_VALUES:
            if sitem.lower() in w_dict:
                position += w_dict[sitem.lower()]
            elif sitem.lower() == "over":
                over_flag = True
                position += 1500
        else:
            if sitem in w_dict:
                if over_flag:
                    dposition += w_dict[sitem]
                elif wrap_flag:
                    nposition += w_dict[sitem]
                else:
                    position += w_dict[sitem]
            elif "{" == sitem[0]:
                wrap_flag = True
                if "}" == sitem[-1]:
                    wrap_flag = False
                    if sitem[1:-1] in w_dict:
                        if over_flag:
                            dposition = w_dict[sitem[1:-1]]
                            if nposition < dposition:
                                position += dposition
                            else:
                                position += nposition
                            over_flag = False
                            nposition = 0
                            dposition = 0
                        else:
                            position += w_dict[sitem[1:-1]]
                    elif not over_flag and sitem[1:] in w_dict:
                        nposition += w_dict[sitem[1:]]
                    elif sitem[1:] in w_dict:
                        dposition += w_dict[sitem[1:]]
                    else:
                        for s in sitem[1:-1]:
                            if s in w_dict:
                                if over_flag:
                                    dposition += w_dict[s]
                                else:
                                    nposition += w_dict[s]
                            elif re.match("[ㄱ-힇]", s):
                                if over_flag:
                                    dposition += w_dict["ㄱ"]
                                else:
                                    nposition += w_dict["ㄱ"]

            else:
                for s in sitem:
                    if s in w_dict:
                        if over_flag:
                            dposition += w_dict[s]
                        elif wrap_flag:
                            nposition += w_dict[s]
                        else:
                            position += w_dict[s]
                    elif re.match("[ㄱ-힇]", s):
                        if over_flag:
                            dposition += w_dict["ㄱ"]
                        elif wrap_flag:
                            nposition += w_dict["ㄱ"]
                        else:
                            position += w_dict["ㄱ"]
    
    if nposition and dposition:
        if nposition > dposition:
            position += nposition
        else:
            position += dposition
    return position


def compute_height(script):
    max_h = 0
    script_items = script.split()
    for sitem in script_items:
        if sitem.lower() == "over":
            h = 2760
        elif "^" in sitem:
            h = 1650
        else:
            h = 1200

        if max_h < h:
            max_h = h

    return max_h


def read_hxml(filename):
    e = ET.parse(filename).getroot()
    body = e.find("BODY")
    section = body.find("SECTION")
    lines = []
    for p in section.findall("P"):
        line = ""
        for i in p.itertext():
            if i.strip():
                line += "%s" % i
        lines.append(line)
    return lines


def str_parsing(filename):
    lines = []
    with codecs.open(filename, encoding="utf-8") as f:
        for line in f:
            if "<CHAR>" in line:
                line = line[:line.find("R>") + 2] + "%s" + line[line.find("</C"):]
            elif "<SCRIPT>" in line:
                line = line[:line.find("T>") + 2] + "%s" + line[line.find("</S"):]
            lines.append(line)

    return lines


def write_hwp(lines, output_filename):
    with codecs.open(output_filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)


def block_parsing(output_filename, gitems, w_dict):
    with codecs.open(output_filename, "w", encoding="utf-8") as f:
        f.write(front)
        i = 0
        j = -1
        flag = False
        for gitem in gitems:
            if i > 0:
                if j != 4:
                    f.write(left_p % "false")
            for item in gitem:
                if item[0] == "char":
                    f.write(left_char)
                    w = item[1].replace("\t", "<TAB />\n")
                    f.write(w)
                    f.write(right_char + "\n")
                elif item[0] == "script":
                    w = compute_width(item[1], w_dict)
                    h = compute_height(item[1])
                    f.write(left_script % (h, w))
                    f.write(item[1])
                    f.write(right_script)
                elif item[0] == "table_start":
                    f.write(left_table)
                    # f.write(left_p)
                    flag=True
                    j += 1
                elif item[0] == "table_end":
                    f.write(right_table)
            i += 1
            if not flag:
                f.write(right_p)
            else:
                flag = False
            if j >= 0:
                j += 1

        f.write(end)


def split_items(str_result):
    gitems = []
    base_items = str_result.split("\n")
    for item in base_items:
        if LTABLE in item:
            gitems.append([("table_start", "")])
            item = item.replace(LTABLE, "")
        elif RTABLE in item:
            gitems.append([("table_end", "")])
            item = item.replace(RTABLE, "")
        items = item.split(LTAG)
        gitem = []
        if "" in items:
            items.remove("")
        for item in items:
            if RTAG in item:
                ritems = item.split(RTAG)
                if "" in ritems:
                    ritems.remove("")
                if ritems:
                    gitem.append(("script", ritems[0]))
                    if len(ritems) == 2:
                        gitem.append(("char", ritems[1]))
            else:
                gitem.append(("char", item))
        gitems.append(gitem)
    return gitems


def block_parsing4pagesplits(output_filename, gitems_list, w_dict):
    with codecs.open(output_filename, "w", encoding="utf-8") as f:
        f.write(front)
        i = 0
        j = -1
        p = 0
        flag = False
        for gitems in gitems_list:
            if p != 0:
                f.write(left_p % "true")
            gitems = split_items(gitems)
            for gitem in gitems:
                if i > 0:
                    if j != 4:
                        f.write(left_p % "false")
                for item in gitem:
                    if item[0] == "char":
                        f.write(left_char)
                        w = item[1].replace("\t", "<TAB />\n")
                        f.write(w)
                        f.write(right_char + "\n")
                    elif item[0] == "script":
                        w = compute_width(item[1], w_dict)
                        h = compute_height(item[1])
                        f.write(left_script % (h, w))
                        f.write(item[1])
                        f.write(right_script)
                    elif item[0] == "table_start":
                        f.write(left_table)
                        # f.write(left_p)
                        flag=True
                        j += 1
                    elif item[0] == "table_end":
                        f.write(right_table)
                i += 1
                if not flag:
                    f.write(right_p)
                else:
                    flag = False
                if j >= 0:
                    j += 1
            p += 1
            i = 0
            j = -1

        f.write(end)


def block_parsing4hml(gitems, w_dict):
    hml = front
    i = 0
    j = -1
    flag = False
    for gitem in gitems:
        if i > 0:
            if j != 4:
                hml += left_p % "false"
        for item in gitem:
            if item[0] == "char":
                hml += left_char
                w = item[1].replace("\t", "<TAB />\n")
                hml += w
                hml += right_char + "\n"
            elif item[0] == "script":
                w = compute_width(item[1], w_dict)
                h = compute_height(item[1])
                hml += left_script % (h, w)
                hml += item[1]
                hml += right_script
            elif item[0] == "table_start":
                hml += left_table
                flag=True
                j += 1
            elif item[0] == "table_end":
                hml += right_table
        i += 1
        if not flag:
            hml += right_p
        else:
            flag = False
        if j >= 0:
            j += 1

    hml += end

    return hml

# 함수를 활용하여 문항 정보 구성 (요청 카운트 만큼, 로그를 활용하여 중복 제거)


def get_gitems(f, count, arguments=None, log=None, etc_info=None, cat_info=None, cat_code=None, polygon=False):
    results = []

    results_stem = []
    results_answer = []
    results_svg = []

    # 인자 값 활용
    try:
        #print("1 arguments", arguments)
        if arguments:
            #print("2 arguments", arguments)
            arguments = dict(arguments)
            #print("3 arguments", arguments)
            stem, answer, comment = f(**arguments)
        else:
            #print("4 arguments", arguments)
            if polygon == False:
                try:
                    stem, answer, comment = f()
                    svg = ""
                except:
                    stem, answer, comment, svg = f()
            else:
                try:
                    stem, answer, comment, svg = f()
                except:
                    stem, answer, comment = f()
                    svg = ""
            
    except Exception:
        # 인자값 활용이 안되는 경우, 함수 에러 출력
        return "FUNC ERROR: %s" % f, log

    # 문항 정보 채우기
    stem = "(문제)\n" + stem


    result = "%s\n%s\n%s" % (stem, answer, comment)
    results.append(result)

    result_stem = "%s" % (stem)
    results_stem.append(result_stem)

    result_answer = "%s\n%s" % (answer, comment)
    results_answer.append(result_answer)

    if type(svg) == list:
        results_svg = svg
    else:
        if svg != "":
            results_svg.append(svg)
        
    return results, results_stem, results_answer, results_svg

def func2hmls(func, count, w_dict, polygon=False):
    #results, logs = get_gitems(func, count, arguments, logs, etc_info, cat_info, cat_code)
    if polygon:
      results, results_stem, results_answer, svgs = get_gitems(func, count, polygon=True)
    else:
      results, results_stem, results_answer, svgs = get_gitems(func, count)

    e = ""

    ##print("zyx results", results)

    if not results:
        e = "NO MORE GENERATED ERR : %s" % func
    elif type(results) == str:
        e = "FUNC ERR : %s" % func
        results = []
    elif count != len(results):
        e = "LIMIT ERR(%s/%s) : %s" % (len(results), count, func)

    hmls = []

    hmls_stem = []
    hmls_answer = []

    for result in results:
        gitems = split_items(result)
        hml = block_parsing4hml(gitems, w_dict)
        hml = base64.b64encode(hml.encode())
        hmls.append(hml)

    for result_stem in results_stem:
        gitems = split_items(result_stem)
        hml = block_parsing4hml(gitems, w_dict)
        hml = base64.b64encode(hml.encode())
        hmls_stem.append(hml)

    for result_answer in results_answer:
        gitems = split_items(result_answer)
        hml = block_parsing4hml(gitems, w_dict)
        hml = base64.b64encode(hml.encode())
        hmls_answer.append(hml)

    #return hmls, e, logs
    return hmls, hmls_stem, hmls_answer, svgs
