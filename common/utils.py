import random

proxies = [
    {'http': 'https://152.67.10.190:8100'},
    {'http': 'https://154.204.58.155:8090'},
    {'http': 'https://198.59.191.234:8080'},
    {'http': 'https://61.28.233.217:3128'},
    {'http': 'https://8.219.176.202:8080'},
    {'http': 'https://200.105.215.22:33630'},
    {'http': 'https://49.0.252.39:8080'},
    {'http': 'https://103.121.149.69:8080'},
    {'http': 'https://94.158.53.145:3128'},
    {'http': 'https://45.61.187.67:4009'},
    {'http': 'https://5.8.53.7:18081'},
    {'http': 'https://178.33.3.163:8080'},
    {'http': 'https://8.219.97.248:80'},
    {'http': 'https://64.225.4.63:9998'},
    {'http': 'https://210.172.199.88:8080'},
    {'http': 'https://210.148.200.2:8080'},
    {'http': 'https://210.148.200.1:8080'},
    {'http': 'https://210.148.141.3:8080'},
    {'http': 'https://64.225.4.29:9499'},
    {'http': 'https://185.20.71.38:443'},
    {'http': 'https://54.37.21.230:3128'},
    {'http': 'https://51.159.115.233:3128'},
    {'http': 'https://213.230.127.93:3128'},
    {'http': 'https://213.241.205.2:3129'},
    {'http': 'https://116.105.25.124:11001'},
    {'http': 'https://143.244.205.72:1080'},
    {'http': 'https://210.148.141.4:8080'},
    {'http': 'https://185.15.172.212:3128'},
    {'http': 'https://210.148.141.1:8080'},
    {'http': 'https://152.67.72.19:8888'},
    {'http': 'https://210.148.141.5:8080'},
    {'http': 'https://210.148.141.2:8080'},
    {'http': 'https://64.225.4.81:9991'},
    {'http': 'https://135.181.114.87:33820'},
    {'http': 'https://115.75.1.184:8118'},
    {'http': 'https://81.12.44.197:3129'},
    {'http': 'https://47.244.32.96:80'},
    {'http': 'https://20.99.187.69:8443'},
    {'http': 'https://40.119.236.22:80'},
    {'http': 'https://159.138.130.126:8999'},
    {'http': 'https://20.69.79.158:8443'},
    {'http': 'https://64.225.8.118:9990'},
    {'http': 'https://103.69.108.78:8191'},
    {'http': 'https://47.254.47.61:77'},
    {'http': 'https://201.229.250.21:8080'},
    {'http': 'https://154.236.189.24:8080'},
    {'http': 'https://83.222.6.82:3128'},
    {'http': 'https://93.177.229.164:9812'},
    {'http': 'https://8.219.74.58:8081'},
    {'http': 'https://77.81.30.250:8080'},
    {'http': 'https://91.121.88.53:80'},
    {'http': 'https://85.114.112.22:8080'},
    {'http': 'https://108.235.184.193:3128'},
    {'http': 'https://50.233.228.147:8080'},
    {'http': 'https://83.151.4.172:57812'},
    {'http': 'https://173.249.198.244:8080'},
    {'http': 'https://103.106.195.41:32650'},
    {'http': 'https://103.236.201.220:3128'},
    {'http': 'https://46.29.165.166:8123'},
    {'http': 'https://41.174.132.58:8080'},
    {'http': 'https://131.161.221.139:80'},
    {'http': 'https://195.133.45.149:7788'},
    {'http': 'https://135.181.78.242:8118'},
    {'http': 'https://45.229.205.243:55555'},
    {'http': 'https://41.74.91.190:7777'},
    {'http': 'https://3.87.27.64:8118'},
    {'http': 'https://181.129.183.19:53281'},
    {'http': 'https://190.61.84.166:9812'},
    {'http': 'https://182.93.85.225:8080'},
    {'http': 'https://79.111.13.155:50625'},
    {'http': 'https://47.74.64.65:3128'},
    {'http': 'https://185.64.208.157:53281'},
    {'http': 'https://205.201.49.132:53281'},
    {'http': 'https://66.70.178.214:9300'},
]


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
