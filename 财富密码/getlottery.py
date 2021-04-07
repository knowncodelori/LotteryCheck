import  requests
import  json
import lotterycheck
url = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1"
r = requests.get(url)
data = json.loads(r.text)
for info in data['value']['list']:
    print("开奖日期", info['lotteryDrawTime'])
    print('开奖期数', info['lotteryDrawNum'])
    print("开奖结果", info['lotteryDrawResult'])
    lotterycheck.lotterycheck(info['lotteryDrawResult'])