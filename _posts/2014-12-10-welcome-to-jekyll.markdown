---
layout: post
title:  "My VHDL Adventure"
date:   2014-12-11
categories: fpga vhdl ece
---

One of my recent VHDL projects needed a 200 Hz signal to multiplex a 4 digit seven segment display. Any faster than 1kHz and the LED's don't have enough time to turn on and any slower we could potentially see flickering.

The solution I arrived upon:
{%highlight vhdl %}

    -- Generate a 200 Hz clock from our 32 MHz clock.
    slow_clk: process(clk)
    BEGIN
        IF rising_edge(clk) THEN

            IF(count(9 downto 0)) = "1111111110" THEN
                clk_200hz <= not clk_200hz;
                count <= (others => '0');
            ELSE
                count <= count + '1';
            END IF;
        END IF;
    END PROCESS;

{%endhighlight%}

Sure enough everything was lit up and there was a success! But then I decided to dig deeper to make sure I was actually hitting my 200 Hz mark. Using a simulation and adding a waveform for my slow_clk signal:

![Waveform screenshow](http://thelag.us/uploads/big/55bfd23a8f8b80be42ea5fa99e6e627f.jpg)

One clock of my alleged 200 Hz clock pulses in 20 micro seconds. Wait a second, that should happen in 0.005 seconds. The clock is way too slow!