import sys
import os
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

HALF_HOUR_DATA = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(HALF_HOUR_DATA)

def load_csv_data(csv_file):
    """
    CSV must have columns: epochTimestamp, kWh, dateTime.
    We parse dateTime in UTC, fill missing 30min intervals with 0 usage.
    """
    df = pd.read_csv(csv_file)
    df['epochTimestamp'] = df['epochTimestamp'].astype(int)
    df['kWh'] = df['kWh'].astype(float)
    df['parsedDT'] = pd.to_datetime(df['dateTime'], utc=True, errors='coerce')
    df.sort_values('parsedDT', inplace=True, ignore_index=True)

    min_dt = df['parsedDT'].iloc[0]
    max_dt = df['parsedDT'].iloc[-1]

    all_times = pd.date_range(start=min_dt, end=max_dt, freq='30T', tz='UTC')
    usage_map = dict(zip(df['epochTimestamp'], df['kWh']))
    known_epochs = set(usage_map.keys())

    results = []
    for t in all_times:
        start_epoch = int(t.timestamp())
        block_kwh = usage_map[start_epoch] if start_epoch in known_epochs else 0.0
        end_epoch = start_epoch + 1800
        start_str = t.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_str   = (t + pd.Timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
        results.append({
            'startEpoch': start_epoch,
            'endEpoch': end_epoch,
            'kWh': float(block_kwh),
            'startDateTime': start_str,
            'endDateTime': end_str
        })
    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python app.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    if not os.path.isfile(csv_file):
        print(f"CSV not found: {csv_file}")
        sys.exit(1)

    HALF_HOUR_DATA = load_csv_data(csv_file)
    print(f"Loaded intervals: {len(HALF_HOUR_DATA)}")
    app.run(debug=True)

