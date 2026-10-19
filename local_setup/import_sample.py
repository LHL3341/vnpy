"""Import the provenance-labelled raw daily sample into the local SQLite database."""
import csv
from datetime import datetime
from zoneinfo import ZoneInfo
from run import WORKSPACE
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BarData
from vnpy.trader.database import get_database


def main():
    bars = []
    with (WORKSPACE / '600000-rqalpha-raw.csv').open() as f:
        for row in csv.DictReader(f):
            bars.append(BarData(symbol='600000', exchange=Exchange.SSE,
                datetime=datetime.fromisoformat(row['datetime']).replace(tzinfo=ZoneInfo('Asia/Shanghai')),
                interval=Interval.DAILY, volume=float(row['volume']), turnover=float(row['turnover']),
                open_price=float(row['open']), high_price=float(row['high']),
                low_price=float(row['low']), close_price=float(row['close']), gateway_name='RQALPHA_SAMPLE'))
    database = get_database()
    database.save_bar_data(bars)
    loaded = database.load_bar_data('600000', Exchange.SSE, Interval.DAILY, bars[0].datetime, bars[-1].datetime)
    assert len(loaded) == len(bars)
    assert loaded[-1].close_price == bars[-1].close_price
    print(f'Imported and read back {len(loaded)} raw daily bars; last close {loaded[-1].close_price}')


if __name__ == '__main__':
    main()
