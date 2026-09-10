网址测试功能网址：https://flourishing-palmier-6da37c.netlify.app/
# 合约爆仓多空观测智能体

独立开发的本地 Web Agent 参赛作品，不属于币安官方产品，不提供交易功能。

## 功能
- 拉取 Binance Futures 公开接口的强平订单、未平仓量和全局多空账户比。
- 按小时统计 24 小时多头/空头爆仓金额。
- 标记大额爆仓事件，生成多空持仓方向趋势和综合 Markdown 报告。
- 接口临时受限时保留演示数据，便于评委在中国或海外网络环境打开页面查看交互。

## 启动
需要 Python 3.10+，无需 API Key：

```bat
cd /d D:\币安作品4
python agent.py web --port 8001
```

浏览器打开：`http://127.0.0.1:8001`

## 数据来源
- Binance Futures REST public API: https://fapi.binance.com
- 强平订单：`/fapi/v1/allForceOrders`
- 未平仓量：`/fapi/v1/openInterest`
- 全局多空账户比：`/futures/data/globalLongShortAccountRatio`

网络或接口限流时，网页会显示演示数据并在报告中注明。正式研究应以实时接口返回为准。

## 说明
页面为上下卡片式布局：顶部概览、中部爆仓/持仓双卡片、大额事件区、底部报告区。资讯检索入口预留在异常事件区，实际联网检索可由评委浏览器或后续 MCP 搜索服务完成。
