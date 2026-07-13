# ✍️ Ứng Dụng Nhận Diện Chữ Số Viết Tay (MNIST)

Ứng dụng giao diện web sử dụng **Streamlit** kết hợp với mô hình học máy mạng nơ-ron đa tầng của thư viện **Scikit-Learn** để phân loại và nhận diện các chữ số viết tay từ 0 đến 9. 

Ứng dụng hỗ trợ 2 phương thức nhập dữ liệu:
1. **Tự tay vẽ số** trực tiếp trên bảng vẽ điện tử.
2. **Tải ảnh từ máy tính lên** (hỗ trợ định dạng PNG, JPG, JPEG).

---

## 🛠️ Yêu Cầu Hệ Thống

Dự án này yêu cầu máy tính của bạn đã được cài đặt sẵn:
* **Python** (Khuyến nghị phiên bản từ 3.11 trở lên).

---

## 🚀 Hướng Dẫn Cài Đặt Và Khởi Chạy

Hãy làm theo các bước tuần tự dưới đây trong cửa sổ dòng lệnh (PowerShell hoặc Command Prompt):

### Bước 1: Di chuyển vào thư mục dự án
Mở cửa sổ dòng lệnh và trỏ đường dẫn tới thư mục chứa mã nguồn của bạn:
```bash
cd đường_dẫn_đến_thư_mục_mnist_web
Bước 2: Cài đặt các thư viện cần thiết
Chạy lệnh sau để tự động tải và cài đặt toàn bộ các thư viện Python bổ trợ cho dự án:
pip install scikit-learn streamlit streamlit-drawable-canvas pillow numpy
Bước 3: Huấn luyện mô hình AI (Tạo file .pkl)
Trước khi chạy giao diện web, bạn cần chạy file huấn luyện để AI học tập trên bộ dữ liệu MNIST gốc và xuất ra file mô hình cục bộ:
python train.py
Bước 4: Khởi chạy ứng dụng Web
Khi đã có file mô hình, bạn chạy lệnh sau để bật giao diện web của ứng dụng lên:
python -m streamlit run app.py

Cấu trúc dự án
mnist_web/
├── train.py          # Mã nguồn tải dữ liệu và huấn luyện mô hình AI
├── app.py            # Mã nguồn xây dựng giao diện Web giao tiếp (Streamlit)
├── mnist_model.pkl   # File mô hình AI sau khi được huấn luyện (Tự động sinh ra)
└── README.md         # File hướng dẫn cài đặt này