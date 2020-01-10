from xml.etree import ElementTree as ET
import requests

r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getStationAndTimeByStationName?StartStation=北京&ArriveStation=上海&UserID=')
result = r.text
print('----北京至上海的火车时刻表----')
root = ET.XML(result)
for node in root.iter('TimeTable'):
    train = '车次:' + node.find('TrainCode').text
    start = '发车站:' + node.find('StartStation').text
    startt = '发车时间:' + node.find('StartTime').text
    arrive = '到达站:' + node.find('ArriveStation').text
    arrivet = '到达时间:' + node.find('ArriveTime').text
    print(train, '----', start, '----', startt, '----', arrive, '----', arrivet)