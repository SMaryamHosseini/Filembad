import requests
import base64

url = "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/refs/heads/main/src/telegram/filembad/messages.txt"

resp = requests.get(url, timeout=10)
lines = resp.text.splitlines()

configs = []
for line in lines:
    line = line.strip()
    if line.startswith(("vmess://", "vless://", "ss://", "trojan://")):
        configs.append(line)

# حذف تکراری‌ها
configs = list(set(configs))

sub_text = "\n".join(configs)
sub_base64 = base64.b64encode(sub_text.encode()).decode()

with open("sub.txt", "w") as f:
    f.write(sub_base64)

print("Subscription updated")
