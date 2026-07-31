import time
import ssl
import paho.mqtt.client as mqtt

# Ở bản 1.6.1, tham số trả về là 'rc' (return code) thay vì 'reason_code'
def on_connect(client, userdata, flags, rc):
    print(f"[MQTT BÁO CÁO] Mã phản hồi từ Broker: {rc}")
    
    # Mã 0 là kết nối thành công, các mã khác là bị từ chối (vd: 5 là Not Authorized)
    if rc == 0:
        print(" CẢNH BÁO: Lỗ hổng! Kết nối ẩn danh thành công.")
    else:
        print(" AN TOÀN: Lớp xác thực đã chặn thành công kẻ gian (Zero-Trust).")

# Dùng cú pháp version 1.6.1
client = mqtt.Client()
client.on_connect = on_connect

# Đi qua đường TLS bảo mật
client.tls_set(ca_certs="D:/mqtt-defense-lab/configs/ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

print("Đang thử kết nối KHÔNG có username/password vào cổng bảo mật 8883...")

try:
    client.connect("localhost", 8883, 60)
    client.loop_start()
    time.sleep(3)
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Lỗi kết nối mạng: {e}")