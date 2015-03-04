---
layout: post
title: Magical Voltage
date: 2014-12-9
categories: engineering
tags:
    - ece
    - fpga
    - vhdl
---

Papilio FPGA 4 Digit 7 Segment display fixed!
I was working on this issue for a while where I'd set the anodes for my 4 digit seven segment display to "1110". Seven segments are low driven which means that a 0 means a digit/segemnt is on and a 1 means off. For some reason I was getting all 4 of my values on no matter what I used:

{%highlight VHDL %}
anodes : OUT STD_LOGIC_VECTOR(3 downto 0);
anodes = "1110"; or = "0101"; etc.
{%endhighlight%}

I made an interesting discovery on the board today where the voltage output was set to 1.2V vs the typical 3.3V. The Papilio and logicstart boards support LVTTL which means that feeding a 1.2V high to these anodes wasn't enough to turn them off. It took me a couple of days to find the cause but I managed to figure it out! Huzzah.

I feel like an idiot ._.
