import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pickle

print("Đang tải tập dữ liệu MNIST từ internet (quá trình này mất khoảng 1-2 phút)...")
# Tải dữ liệu MNIST gốc
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target

# Chuẩn hóa dữ liệu về khoảng [0, 1]
X = X / 255.0

# Chia tập dữ liệu huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

print("Đang huấn luyện mô hình AI (MLPClassifier)...")
# Khởi tạo mô hình mạng nơ-ron
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=20, alpha=1e-4,
                      solver='adam', verbose=True, random_state=1, learning_rate_init=.001)

# Huấn luyện
model.fit(X_train, y_train)

# Đánh giá độ chính xác
score = model.score(X_test, y_test)
print(f"\nHuấn luyện xong! Độ chính xác trên tập Test: {score*100:.2f}%")

# Lưu mô hình thành file cục bộ tên là mnist_model.pkl
model_name = "mnist_model.pkl"
with open(model_name, 'wb') as f:
    pickle.dump(model, f)
    
print(f"Đã xuất mô hình thành công ra file: {model_name}")