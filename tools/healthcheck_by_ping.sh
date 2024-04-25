#!/bin/sh

HOST=10.207.247.55

GREEN='\033[0;32m'
NC='\033[0m'

#ping 192.168.9.93 #
echo "[+] Starting..."
if [ -f "$1" ]; then
  echo "[+] IPs file: $1"
else
  echo 'File does not exist.'
  exit 2;
fi

while IFS= read -r line; do
  ip=`echo "$line" | xargs`
  if ( ping -c1 $ip 1>/dev/null 2>/dev/null ); then
    echo "$ip: online"
    echo "$ip: online" >> "healthcheck_results.txt"
  else
    echo "$ip: offline"
    echo "$ip: offline" >> "healthcheck_results.txt"
  fi
done < "$1"
