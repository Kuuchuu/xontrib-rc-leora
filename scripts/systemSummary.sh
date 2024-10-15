#!/usr/bin/env bash
clear && (hyfetch || uwufetch || neofetch || fastfetch || screenfetch || macchina || nerdfetch)
uptime | awk -F'[ ,]+' '{print "System load: " $(NF-2) ", " $(NF-1) ", " $NF}' | awk '{print "  ❥ "$0}'
echo "Disk Usage:" | awk '{print "  ❥ "$0}'
df -h / | awk 'NR==1{sub(/Filesystem/, "Filesystem    "); print "      > "$0; next} {print "          ✦ "$0}'

echo "  ❥ Temperature:"
wifi_temp=$(sensors | grep -oP 'temp1: *\+\K[0-9.]+')
nvme_temp=$(sensors | grep -oP 'Composite: *\+\K[0-9.]+')
cpu_temp=$(sensors | grep -oP 'Tctl: *\+\K[0-9.]+')
gpu_temp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits | head -1)

echo "      > CPU: $(echo "$cpu_temp" | awk '{print ($1 * 1.8) + 32 "°F"}')"
echo "      > GPU: $(echo "$gpu_temp" | awk '{print ($1 * 1.8) + 32 "°F"}') | Crit: 194°F | Shutdown: 215.6°F"
echo "      > NVMe SSD: $(echo "$nvme_temp" | awk '{print ($1 * 1.8) + 32 "°F"}')"
echo "      > WiFi Adapter: $(echo "$wifi_temp" | awk '{print ($1 * 1.8) + 32 "°F"}')"

echo "Processes:" | awk '{print "  ❥ "$0}'
ps -e | wc -l | awk '{print "      > "$0}'
echo "Network Information:" | awk '{print "  ❥ "$0}'
ip -4 addr | awk '/inet/ && !/127.0.0.1/ {print $2, $NF}' | awk '{print "      > "$0}'
uptime | awk -F'[ ,]+' '{print "Users logged in: " $(NF-6)}' | awk '{print "  ❥ "$0}'
who | awk '{print "      > "$0}'
echo ""
