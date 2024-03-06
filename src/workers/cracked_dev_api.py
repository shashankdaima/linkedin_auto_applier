from ..config import CRACKED_DEV_API_KEY
import requests
class CrackedDevApi:
    def get_cracked_dev_jobs(pageNo:int, pageSize:int):
        url = f'https://api.crackeddevs.com/v1/get-jobs?limit={pageSize}&page={pageNo}'
        headers = {
            'api-key':CRACKED_DEV_API_KEY ,  # API KEY HERE
        }

        response = requests.get(url, headers=headers)

        if response.ok:
            data = response.json()
            print(data)
            return data
        else:
            print("HTTP-Error:", response.status_code)
