from spider.decode import DecodeEncry
# from decode import DecodeEncry
import requests
import json

class sipder:
    # 定期更改
    def __init__(self):
        self.synct = '1607567197.490'
        self.api_url = "/app/keywordDetail"
        self.cookie = 'qm_check=SxJXQEUSChd2fHd1dRQQfmZ5dHlxEHJSdF9LU1EYd2RoEAEABQUXZlkZdF1KVVNEA3QBARVBQW8MbwQYQENvBW8AGRcbEFNRVVdTEgoSABwAHAUbAhwJEkk%3D; gr_user_id=d89f89ac-967b-428b-8329-4e91e98c1f4d; grwng_uid=8004ce3d-7581-4e9b-924e-c6f289c17993; ada35577182650f1_gr_last_sent_cs1=qm10678341965; aso_ucenter=f3baFTLd6FkmFGWdSbE7Vru42WjMtkZImlnRYjGYwFomlMeG8dWkFHtSwhHgcldsWg; USERINFO=OJ%2Br7pc4ncKuA%2Bc7yukM%2FkFVJS1d7100SYrehk8tNoxUybVlmCI5BuORUQe1SNnrjWRAm4Ey5ZWoaFmG9iV7oGAklcF56TUmL0Z5MulVRdHLWbS61KhbE%2F9StoXNBdNmFxAfX5PWDrem6fTCfg72tg%3D%3D; PHPSESSID=77crnl2eletp05aurvlhi7q73m; ada35577182650f1_gr_session_id=f65b5f6f-e25e-45ae-a8dd-2a55b5a1ff72; ada35577182650f1_gr_last_sent_sid_with_cs1=f65b5f6f-e25e-45ae-a8dd-2a55b5a1ff72; ada35577182650f1_gr_cs1=qm10678341965; ada35577182650f1_gr_session_id_f65b5f6f-e25e-45ae-a8dd-2a55b5a1ff72=true; synct=1607567197.490; syncd=-229'
    def start(self, appid):
        params = {
            'country': 'cn',
            "version": 'ios12',  # 设备类型
            'appid': f'{appid}'
        }
        analysis = DecodeEncry().get_analysis(self.synct, self.api_url, params)

        url = f'https://api.qimai.cn/app/keywordDetail?analysis={analysis}&country=cn&version=ios12&appid={appid}'

        head = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55',
            'accept':'application/json, text/plain, */*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie':self.cookie
        }

        data = requests.get(url,headers = head)
        data_dir = json.loads(data.text)
        json_str = json.dumps(data_dir)
        with open('data/test_data.json', 'w') as json_file:
            json_file.write(json_str)
        return True

if __name__ == '__main__':
    sipder().start('518213356')