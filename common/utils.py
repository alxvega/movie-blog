import random

proxies = [
    {'http': 'https://129.154.225.163:8100'},
    {'http': 'https://64.225.8.82:9995'},
    {'http': 'https://20.210.38.220:3129'},
    {'http': 'https://5.8.53.7:18081'},
    {'http': 'https://178.33.3.163:8080'},
    {'http': 'https://210.172.199.88:8080'},
    {'http': 'https://54.37.21.230:3128'},
    {'http': 'https://93.177.73.122:8888'},
    {'http': 'https://210.148.141.1:8080'},
    {'http': 'https://176.99.2.43:1081'},
    {'http': 'https://91.233.115.105:31280'},
    {'http': 'https://103.151.177.106:80'},
    {'http': 'https://54.39.183.193:3128'},
    {'http': 'https://85.234.126.107:55555'},
    {'http': 'https://119.13.103.211:83'},
    {'http': 'https://8.219.176.202:8080'},
    {'http': 'https://49.0.252.39:8080'},
    {'http': 'https://190.61.88.147:8080'},
    {'http': 'https://115.96.208.124:8080'},
    {'http': 'https://179.96.28.58:80'},
    {'http': 'https://107.179.9.238:3128'},
    {'http': 'https://104.223.164.180:3128'},
    {'http': 'https://79.137.204.108:4444'},
    {'http': 'https://210.148.200.3:8080'},
    {'http': 'https://210.148.141.4:8080'},
    {'http': 'https://152.200.190.58:999'},
    {'http': 'https://191.103.219.225:48612'},
    {'http': 'https://144.217.240.185:9300'},
    {'http': 'https://51.79.50.31:9300'},
    {'http': 'https://103.162.30.111:20000'},
    {'http': 'https://103.169.254.164:8061'},
    {'http': 'https://157.230.241.133:36835'},
    {'http': 'https://68.183.185.62:80'},
    {'http': 'https://8.209.249.96:2080'},
    {'http': 'https://65.109.86.182:33229'},
    {'http': 'https://43.251.116.38:45787'},
    {'http': 'https://195.8.52.158:6666'},
    {'http': 'https://190.26.201.194:8080'},
    {'http': 'https://115.144.101.201:10001'},
    {'http': 'https://34.140.70.242:8080'},
    {'http': 'https://210.148.200.2:8080'},
    {'http': 'https://210.148.200.1:8080'},
    {'http': 'https://200.105.215.22:33630'},
    {'http': 'https://201.229.250.21:8080'},
    {'http': 'https://152.67.72.19:8888'},
    {'http': 'https://165.227.81.188:9958'},
    {'http': 'https://65.108.230.239:42899'},
    {'http': 'https://20.219.112.20:80'},
    {'http': 'https://103.169.35.129:3128'},
    {'http': 'https://80.14.219.107:3128'},
    {'http': 'https://152.32.68.171:65535'},
    {'http': 'https://65.108.230.238:45977'},
    {'http': 'https://94.232.11.178:46449'},
    {'http': 'https://54.39.188.64:3128'},
    {'http': 'https://64.225.4.29:9499'},
    {'http': 'https://213.241.205.2:3129'},
    {'http': 'https://64.225.4.81:9991'},
    {'http': 'https://175.100.72.95:57938'},
    {'http': 'https://167.172.238.15:9992'},
    {'http': 'https://148.244.170.54:32650'},
    {'http': 'https://195.133.45.149:7788'},
    {'http': 'https://27.76.81.191:5009'},
    {'http': 'https://185.142.64.228:8080'},
    {'http': 'https://103.171.183.201:8181'},
    {'http': 'https://103.121.120.178:32650'},
    {'http': 'https://188.0.147.102:3128'},
    {'http': 'https://198.59.191.234:8080'},
    {'http': 'https://8.219.97.248:80'},
    {'http': 'https://210.148.141.3:8080'},
    {'http': 'https://157.245.27.9:3128'},
    {'http': 'https://213.136.101.36:3128'},
    {'http': 'https://210.148.141.5:8080'},
    {'http': 'https://210.148.141.2:8080'},
    {'http': 'https://40.119.236.22:80'},
    {'http': 'https://93.157.163.66:35081'},
    {'http': 'https://91.150.189.122:30389'},
    {'http': 'https://95.217.104.21:17344'},
    {'http': 'https://54.39.180.76:3128'},
    {'http': 'https://204.157.240.56:999'},
    {'http': 'https://213.230.68.211:3128'},
    {'http': 'https://20.210.26.15:3129'},
    {'http': 'https://103.111.82.82:9812'},
    {'http': 'https://217.219.74.130:8888'},
    {'http': 'https://64.225.8.132:9979'},
    {'http': 'https://5.196.139.54:3128'},
    {'http': 'https://103.121.149.69:8080'},
    {'http': 'https://115.144.102.39:10080'},
    {'http': 'https://129.24.194.69:8000'},
    {'http': 'https://51.159.115.233:3128'},
    {'http': 'https://159.138.130.126:8999'},
    {'http': 'https://34.229.213.84:8118'},
    {'http': 'https://202.180.20.10:55443'},
    {'http': 'https://123.60.139.197:59394'},
    {'http': 'https://143.44.191.108:8080'},
    {'http': 'https://188.64.132.59:3127'},
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
