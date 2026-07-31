import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Dashboard kết nối TLS thành công! Đang chờ dữ liệu an toàn...")
        client.subscribe("iot/sensor/#")
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):
    print(f"[DỮ LIỆU ĐẾN] Topic: {msg.topic} | Payload: {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set("dashboard", "123456")

# --- CẤU HÌNH TLS ---
client.tls_set(ca_certs="D:/mqtt-defense-lab/configs/ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

client.on_connect = on_connect
client.on_message = on_message

# --- KẾT NỐI VÀO CỔNG 8883 ---
client.connect("localhost", 8883, 60)
client.loop_forever()