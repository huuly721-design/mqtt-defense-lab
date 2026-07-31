import paho.mqtt.client as mqtt
import time
import json
import random
import ssl # Thêm thư viện TLS

data = {
    "device": "ESP32_NhietDo",
    "temp": random.randint(25, 35),
    "humidity": random.randint(60, 90)
}
payload = json.dumps(data)

client = mqtt.Client()
client.username_pw_set("sensor", "123456")

# --- CẤU HÌNH TLS ---
client.tls_set(ca_certs="D:/mqtt-defense-lab/configs/ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True) # Bỏ qua check tên miền khắt khe trong lab

# --- KẾT NỐI VÀO CỔNG 8883 ---
client.connect("localhost", 8883, 60)

client.loop_start()
print("Sensor đang kết nối (Bảo mật TLS) và gửi dữ liệu...")
client.publish("iot/sensor/nhietdo", payload)
print(f"Đã gửi (Mã hóa): {payload}")
time.sleep(2)
client.loop_stop()
client.disconnect()