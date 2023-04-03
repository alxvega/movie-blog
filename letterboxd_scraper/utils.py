import random

proxies = [
    {"http": "https://200.105.215.22:33630"},
    {"http": "https://200.54.194.13:53281"},
    {"http": "https://190.104.245.86:8080"},
    {"http": "https://159.89.132.167:8989"},
    {"http": "https://93.90.82.43:3128"},
    {"http": "https://204.2.218.145:8080"},
    {"http": "https://201.229.250.21:8080"},
    {"http": "https://1.214.62.71:8000"},
    {"http": "https://31.186.239.244:8080"},
    {"http": "https://49.0.2.242:8090"},
    {"http": "https://130.41.101.105:8080"},
    {"http": "https://115.144.101.200:10000"},
    {"http": "https://118.27.113.167:8080"},
    {"http": "https://165.246.148.50:8080"},
    {"http": "https://46.101.13.77:80"},
    {"http": "https://135.181.14.45:5959"},
    {"http": "https://146.190.94.249:8080"},
    {"http": "https://46.4.242.214:1337"},
    {"http": "https://162.55.188.41:8020"},
    {"http": "https://5.9.149.118:40000"},
    {"http": "https://5.189.184.6:80"},
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
