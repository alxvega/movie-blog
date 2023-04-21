import random

proxies = [{'http': 'https://172.104.117.89:80'}, {'http': 'https://8.219.176.202:8080'}, {'http': 'https://190.61.88.147:8080'}, {'http': 'https://82.66.18.27:8080'}, {'http': 'https://115.144.102.39:10080'}, {'http': 'https://210.172.199.88:8080'}, {'http': 'https://115.144.101.201:10001'}, {'http': 'https://45.136.58.51:8888'}, {'http': 'https://43.134.211.34:3128'}, {'http': 'https://208.82.63.6:3128'}, {'http': 'https://104.171.160.138:3128'}, {'http': 'https://13.212.131.211:3128'}, {'http': 'https://178.33.3.163:8080'}, {'http': 'https://201.229.250.21:8080'}, {'http': 'https://20.3.76.94:8080'}, {'http': 'https://20.121.242.93:3128'}, {'http': 'https://40.119.236.22:80'}, {'http': 'https://124.156.139.46:4780'}, {'http': 'https://188.127.249.9:20255'}, {'http': 'https://64.225.4.12:9991'}, {'http': 'https://46.209.106.202:3128'}, {'http': 'https://186.121.235.66:8080'}, {'http': 'https://3.1.51.149:3128'}, {'http': 'https://113.53.231.133:3129'}, {'http': 'https://8.219.97.248:80'}, {'http': 'https://43.156.100.152:80'}, {'http': 'https://158.160.56.149:8080'}, {'http': 'https://202.72.220.83:8080'}, {'http': 'https://110.34.3.229:3128'}, {'http': 'https://65.108.230.238:45977'}, {'http': 'https://43.135.13.39:8080'}, {'http': 'https://23.236.70.102:45787'}, {'http': 'https://64.225.4.29:9499'}, {'http': 'https://68.132.12.228:8888'}, {'http': 'https://82.148.6.193:80'}, {'http': 'https://193.111.124.101:8080'}, {'http': 'https://62.138.7.104:8646'}, {'http': 'https://200.105.215.22:33630'}, {'http': 'https://41.65.236.43:1976'}, {'http': 'https://51.91.118.79:8080'}, {'http': 'https://167.99.116.111:8000'}, {'http': 'https://167.71.199.211:39909'}, {'http': 'https://45.61.187.67:4007'}, {'http': 'https://65.108.230.239:42899'}, {'http': 'https://78.38.93.22:3128'}, {'http': 'https://81.12.44.197:3129'}, {'http': 'https://103.191.155.30:8085'}, {'http': 'https://129.154.225.163:8100'}, {'http': 'https://68.183.53.101:9918'}, {'http': 'https://200.25.254.193:54240'}, {'http': 'https://47.91.45.198:8888'}, {'http': 'https://8.209.64.208:8080'}, {'http': 'https://49.0.246.130:45554'}, {'http': 'https://8.209.243.173:443'}, {'http': 'https://174.138.184.82:46706'}, {'http': 'https://213.83.46.204:3128'}, {'http': 'https://43.229.148.70:8080'}, {'http': 'https://84.214.150.146:8080'}, {'http': 'https://95.216.170.84:8080'}, {'http': 'https://65.109.170.164:8080'}, {'http': 'https://198.44.189.98:45787'}]


def generate_user_agents(version_range: tuple):
    all_uas = {
        "windows": [],
        "mac_os": [],
        "linux": [],
        "ios_mobile": [],
    }
    for version in range(version_range[0], version_range[1] + 1):
        linux = [
            f"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
            f"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (X11; Linux x86_64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            f"Mozilla/5.0 (X11; Linux i686; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
        ]
        windows = [
            f"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{version}.0) Gecko/20100101 Firefox/110.0",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (Windows NT 10.0; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.1462.54",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 OPR/94.0.0.0",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.1518.61",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.1462.76",
            f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.1518.70",
            f"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
            f"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 OPR/93.0.0.0",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.1518.55",
        ]
        mac_os = [
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 YaBrowser/22.11.7.42 Yowser/2.5 Safari/537.f36",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:{version}.0) Gecko/20100101 Firefox/{version}.0",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        ]

        ios_mobile = [
            f"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{version}.0 Mobile/15E148 Safari/605.1.15",
            f"Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{version}.0 Mobile/15E148 Safari/605.1.15",
            f"Mozilla/5.0 (iPod touch; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/{version}.0 Mobile/15E148 Safari/605.1.15",
            f"Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/{version}.0",
            f"Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:{version}.0) Gecko/{version}.0 Firefox/{version}.0",
        ]
        all_uas["windows"].extend(windows)
        all_uas["mac_os"].extend(mac_os)
        all_uas["linux"].extend(linux)
        all_uas["ios_mobile"].extend(ios_mobile)

    return all_uas


def get_random_user_agent(all_uas):
    selected_key = random.choice(list(all_uas.keys()))
    selected_index = random.randint(0, len(all_uas[selected_key]) - 1)
    return all_uas[selected_key][selected_index]


def get_proxy_session():
    return random.choice(proxies)
