A tool for taking smart-meter data and simulating the effect for the period
covered by the data of adding battery storage to the system, and changing
the tariffs to allow for off-peak charging of said battery.

The import data is the format that is exported through https://glowmarkt.com/,
which you can link to your smart meter with the Bright app. This format may
be standard, I've no idea, but in any case it's pretty simple.

I wanted to quantify the effect of adding a battery ESS to our house, which
this tool seems to do.

I say "seems to" because this was also an experiment in using ChatGPT to write
a tool of this sort. I know various programming languages well, but I have only
a passing familiarity with JS and front-end development. A few things I
requested it failed to achieve properly and a required a bit of hacking to make
it look as I wanted.. Still, I spent about 5 hours on it and the results appear
to be useful.

It doesn't always respond quite as desired to state changes. You might find
you need to change a variable to make it respond properly, notably after a
refresh. This might have improved after moving to a single page.

Please do submit any improvements, of which I'm sure there are loads.

To run, simply open `battery_model.html` in a web browser, and click to load an
appropriate CSV file. Set the battery to a non-zero value for it to have any
effect.

A suitable CSV file looks like `test_data.csv` (this is what glowmarkt exports).

It uses Chart.js to render the charts, which is should download as needed.

![Screenshot of running page](/screenshot.png?raw=true "Screenshot")
