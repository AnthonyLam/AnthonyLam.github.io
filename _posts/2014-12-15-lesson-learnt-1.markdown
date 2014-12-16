---
layout: post
title: Lesson Learnt 1
date: 2014-12-15
categories: fpga vhdl ece lessonlearnt
---

# Use Your Signals
It's not often I get to spend hours upon hours fixing simple mistakes in my code but today was one such lucky day.

The problem I had was Xilinx ISE constantly removing bits and pieces of my code in an effort to "optimize" it and it was up to me to figure out why in the hell the program was getting rid of it.

The infringing code:
{%highlight VHDL %}
anode_flicker: process(clk_200hz)
   BEGIN
       CASE anode_select(3 downto 0) IS
           WHEN "1110" =>
               anode_select <= "1101";
               segments <= cur_segment;
           WHEN "1101" =>
               anode_select <= "1011";
               segments <= cur_segment;
           WHEN "1011" =>
               anode_select <= "0111";
               segments <= cur_segment_high;
           WHEN "0111" =>
               anode_select <= "1110";
               segments <= cur_segment_high;
           WHEN OTHERS =>
               anode_select <= "1110";
       END CASE;
       anodes <= anode_select;
   END PROCESS;
{%endhighlight %}

As it turned out I forgot something extremely important that I had already learnt: Use the signals you specify in your process. In this case I left out the usage of `clk_200hz`. The process was being triggered whenever there was a trigger coming from clk_200hz but that's literally always happening. What needed to be done was narrow the trigger down to either a rising or falling edge of the signal like so:

{%highlight VHDL %}
anode_flicker: process(clk_200hz)
   BEGIN

        IF rising_edge(clk_200hz) THEN -- HERE
           CASE anode_select(3 downto 0) IS
               WHEN "1110" =>
                   anode_select <= "1101";
                   segments <= cur_segment;
               WHEN "1101" =>
                   anode_select <= "1011";
                   segments <= cur_segment;
               WHEN "1011" =>
                   anode_select <= "0111";
                   segments <= cur_segment_high;
               WHEN "0111" =>
                   anode_select <= "1110";
                   segments <= cur_segment_high;
               WHEN OTHERS =>
                   anode_select <= "1110";
           END CASE;
       END IF;                              -- AND HERE
       anodes <= anode_select;
   END PROCESS;
{%endhighlight%}
