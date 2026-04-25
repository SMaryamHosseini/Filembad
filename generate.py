import requests
import base64
import re

url = "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/refs/heads/main/src/telegram/filembad/messages.txt"

resp = requests.get(url, timeout=10)
text = resp.text

# استخراج همه کانفیگ‌ها
configs = re.findall(r'(vmess://[^\s]+|vless://[^\s]+|ss://[^\s]+|trojan://[^\s]+)', text)

# حذف تکراری‌ها
configs = list(set(configs))

print(f"Found {len(configs)} configs")

# اگر هیچی پیدا نشد، فایل خالی نساز
if not configs:
    raise ValueError("No configs found!")

sub_text = "\n".join(configs)
sub_base64 = base64.b64encode(sub_text.encode()).decode()

with open("sub.txt", "w") as f:
    f.write(sub_base64)

print("Subscription updated")
