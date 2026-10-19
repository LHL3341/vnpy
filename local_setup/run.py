"""Launch the local research desktop without brokerage gateways."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / 'local_workspace'
WORKSPACE.mkdir(exist_ok=True)
(WORKSPACE / '.vntrader').mkdir(exist_ok=True)
os.chdir(WORKSPACE)

from vnpy.trader.setting import SETTINGS
SETTINGS.update({'font.family': 'PingFang SC', 'database.timezone': 'Asia/Shanghai',
                 'database.name': 'sqlite'})


def main():
    from vnpy.event import EventEngine
    from vnpy.trader.engine import MainEngine
    from vnpy.trader.ui import MainWindow, create_qapp
    from vnpy_ctabacktester import CtaBacktesterApp
    from vnpy_datamanager import DataManagerApp
    from vnpy_portfoliostrategy import PortfolioStrategyApp

    app = create_qapp()
    events = EventEngine()
    engine = MainEngine(events)
    engine.add_app(CtaBacktesterApp)
    engine.add_app(DataManagerApp)
    engine.add_app(PortfolioStrategyApp)
    window = MainWindow(engine, events)
    window.setWindowTitle('VeighNa 研究工作台 · 本地历史研究 · 未连接券商')
    window.resize(1360, 880)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
