import random

proxies = [
    {'http': 'https://8.219.176.202:8080'},
    {'http': 'https://152.67.10.190:8100'},
    {'http': 'https://47.244.32.96:80'},
    {'http': 'https://190.61.88.147:8080'},
    {'http': 'https://115.144.101.201:10001'},
    {'http': 'https://198.59.191.234:8080'},
    {'http': 'https://80.14.219.107:3128'},
    {'http': 'https://40.119.236.22:80'},
    {'http': 'https://45.136.238.69:8080'},
    {'http': 'https://66.70.178.214:9300'},
    {'http': 'https://37.120.192.154:8080'},
    {'http': 'https://200.105.215.22:33630'},
    {'http': 'https://116.105.25.124:11001'},
    {'http': 'https://94.131.108.61:8443'},
    {'http': 'https://5.161.110.95:50001'},
    {'http': 'https://20.99.187.69:8443'},
    {'http': 'https://174.138.184.82:46706'},
    {'http': 'https://82.148.6.193:80'},
    {'http': 'https://8.219.97.248:80'},
    {'http': 'https://167.172.238.15:9992'},
    {'http': 'https://168.11.52.41:8080'},
    {'http': 'https://195.158.18.236:3128'},
    {'http': 'https://115.96.208.124:8080'},
    {'http': 'https://187.130.139.197:8080'},
    {'http': 'https://196.202.210.73:32650'},
    {'http': 'https://138.201.132.168:8118'},
    {'http': 'https://103.162.54.246:8080'},
    {'http': 'https://49.156.47.162:8080'},
    {'http': 'https://118.70.109.148:55443'},
    {'http': 'https://188.163.170.130:41209'},
    {'http': 'https://202.150.132.53:8080'},
    {'http': 'https://213.230.126.26:3128'},
    {'http': 'https://159.138.130.126:8999'},
    {'http': 'https://89.237.21.119:3128'},
    {'http': 'https://103.121.149.69:8080'},
    {'http': 'https://65.108.230.238:45977'},
    {'http': 'https://204.2.218.145:8080'},
    {'http': 'https://24.156.198.241:8080'},
    {'http': 'https://64.225.8.132:9979'},
    {'http': 'https://71.19.248.67:8001'},
    {'http': 'https://165.227.81.188:9958'},
    {'http': 'https://64.225.4.29:9499'},
    {'http': 'https://45.136.58.51:8888'},
    {'http': 'https://43.229.148.70:8080'},
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
