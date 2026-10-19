"""Connectivity check using an upstream demo, not an A-share strategy validation."""
from datetime import datetime
import json
from run import WORKSPACE
from vnpy.trader.constant import Interval
from vnpy_ctastrategy.backtesting import BacktestingEngine
from vnpy_ctastrategy.strategies.double_ma_strategy import DoubleMaStrategy

engine = BacktestingEngine()
engine.set_parameters(vt_symbol='600000.SSE', interval=Interval.DAILY,
    start=datetime(2025, 1, 1), end=datetime(2026, 9, 30),
    rate=0.0003, slippage=0.01, size=1, pricetick=0.01, capital=1000000)
engine.add_strategy(DoubleMaStrategy, {})
engine.load_data()
assert len(engine.history_data) == 424
engine.run_backtesting()
result = engine.calculate_result()
assert result is not None and not result.empty
stats = engine.calculate_statistics(output=False)
assert stats['total_trade_count'] > 0
result.to_csv(WORKSPACE / 'connectivity-backtest.csv')
report = {'purpose': 'engine connectivity, NOT A-share rule or profitability validation',
          'strategy': 'upstream DoubleMaStrategy (permits short positions)',
          'bars': len(engine.history_data), 'trades': int(stats['total_trade_count']),
          'days': int(stats['total_days']), 'passed': True}
(WORKSPACE / 'acceptance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(report)
