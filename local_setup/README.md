# 本地 VeighNa 研究环境

上游：https://github.com/vnpy/vnpy
个人 fork：https://github.com/LHL3341/vnpy

双击根目录 `start-research.command` 打开官方桌面平台。本地配置和 SQLite 数据库保存在 `local_workspace/.vntrader`，不使用个人主目录的已有账户配置。

安装模块：CTA 回测、数据管理、组合策略。启动入口不加载任何券商网关。组合策略界面在未接入行情和网关时不能执行持续模拟交易。

数据管理中使用 `600000.SSE`、日线 `d` 查看已导入的历史样本。样本来自已有 RQAlpha 官方历史 bundle，包含 2025-01-02 至 2026-09-30 的 424 根未复权日线，导入来源记录在 `local_workspace/import-source.json`。

通用 CTA 回测用于界面和引擎连通性验证，不代表 A 股 T+1、涨跌停、整手、分红和税费已完整适配。原有 RQAlpha 验收结果保留，不能将两个引擎的收益直接等同。未添加或优化策略。

环境复现：

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r local_setup/requirements.lock
.venv/bin/python local_setup/import_sample.py
./start-research.command
```

样本 CSV 为本地生成数据，不提交到仓库；复现导入需要先准备该文件。

推荐在 Finder 中双击根目录 `VeighNa Research.app`；`start-research.command` 是终端备用入口。应用启动后，左侧工具栏打开「数据管理」或「CTA回测」。这是原生桌面应用，旧的 localhost:8520 页面仍是之前的研究界面。

本机验证结果（2026-10-19）：

- VeighNa 4.5.0、Python 3.12 和官方模块安装成功，桌面主窗口、数据管理和 CTA 回测窗口能够打开。
- `import_sample.py` 导入并读回 424 根日线，末条收盘价 9.48。
- `check_backtest.py` 调用官方 DoubleMaStrategy 完成 424 个交易日、29 笔成交的连通性验证；结果保存在本地 `acceptance.json` 与 `connectivity-backtest.csv`。
- 上述回测由脚本运行，尚未完成逐项桌面交互验收；数据管理树的样本展开显示也需继续检查。
- 样例允许做空；此结果不代表 A 股交易规则、实盘或实时模拟验收通过。

重新运行引擎验证：

```sh
.venv/bin/python local_setup/check_backtest.py
```
