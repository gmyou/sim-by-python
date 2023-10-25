import json, pandas as pd
# test.json 내용: [{"name":"Jack","age":26},{"name":"Ace","age":87}]
 
with open('test.json') as f:
    js = json.loads(f.read()) ## json 라이브러리 이용
df = pd.DataFrame(js)
df = pd.read_json('test.json') ## pd.read_json 이용
 
## orient
df.to_json() # default : orient='columns'
# Output : '{"name":{"0":"Jack","1":"Ace"},"age":{"0":26,"1":87}}'
df.to_json(orient='records')
# Output : '[{"name":"Jack","age":26},{"name":"Ace","age":87}]'
df.to_json(orient='index')
# Output : '{"0":{"name":"Jack","age":26},"1":{"name":"Ace","age":87}}'
 
## json으로 쓰기
df.to_json('write.json',orient='index')
## -> pd.read_json()으로 json을 읽으면 orient를 자동으로 인식