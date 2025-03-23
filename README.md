A tool for taking smart-meter data and simulating the effect for the period
covered by the data of adding battery storage to the system, and changing
the tariffs to allow for off-peak charging of said battery.

The import data is the format that is exported through https://glowmarkt.com/,
which you can link to your smart meter with the Bright app. This format may
be standard, I've no idea, but in any case it's pretty simple.

I wanted to quantify the effect of adding a battery ESS to our house, which
this tool seems to do.

I say "seems to" because this was also an experiment in using ChatGPT to write
a tool of this sort. I know python well, but I have only a passing familiarity with
JS and front-end development. A few things I requested it failed to achieve
properly and I lack the skills and inclincation to debug it properly.
Still, I spent about 3 hours on it and the results appear to be useful.

Please do submit any improvements, of which I'm sure there are loads.

To run, clone the repo, install the requirements (`pip install -r requirements.txt`)
and run with:

```
python app.py smart_meter_electricity_data.csv
```

where `smart_meter_electricity_dat.csv` is a suitable CSV file that looks like `test_data.csv` (this is what glowmarkt exports).

You can then go to a web browser and navigate to `http://127.0.0.1:5000/`.
