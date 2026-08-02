# 🛡️ ĐỒ ÁN: Mô phỏng phòng thủ MQTT trong môi trường lab

> **Thông tin Đồ án**
> * **Môn học:** Bảo mật trong IoT
> * **Lớp học phần:** 253INT441001
> * **Giảng viên hướng dẫn:** Hồ Nhựt Minh
> * **Sinh viên thực hiện:** Lê Hữu Lý 
> * **MSSV:** 231A011195

---

## 🚀 Hướng dẫn Cài đặt và Chạy hệ thống

### 1. Yêu cầu hệ thống (Prerequisites)
- 💻 **Hệ điều hành:** Windows / Linux / macOS
- 🐍 **Môi trường:** Đã cài đặt **Python 3.8** trở lên
- 🌐 **MQTT Broker:** Đã cài đặt **Eclipse Mosquitto Broker 2.0.x** (hỗ trợ TLS)
- 🛠️ **IDE/Editor:** Đã cài đặt **Visual Studio Code** (phiên bản mới nhất)
- 🔐 **Công cụ hỗ trợ:** Đã cài đặt **OpenSSL** NẾU MUỐN sinh bộ khóa và chứng chỉ giả lập mới.

---

### 2. Cài đặt thư viện Python
** Mở Terminal trong Visual Studio Code và chạy lệnh cài đặt thư viện `paho-mqtt` phiên bản tương thích: **
---

pip install paho-mqtt==1.6.1

### 3. mở CMD và khởi chạy Folder dự án và Service Mosquitto 


**Ví dụ đặt cách chạy dự án bao gồm source code trong ổ D**: 

 D: && cd \mqtt-defense-lab\configs && "C:\Program Files\Mosquitto\mosquitto.exe" -c mosquitto.conf -v
---
### 4. Mở Folder mqtt-defense-lab trên visual code và bật terminal chạy lần lượt các kịch bản Python:

python src/subscriber.py

python src/publisher.py

python src/unauthorized_client.py

### 5. Quan sát các logs trên terminal khi bật cùng scripts
---

