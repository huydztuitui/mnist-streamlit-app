import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pickle
import numpy as np
from PIL import Image

st.set_page_config(page_title="MNIST Local App", layout="centered")
st.title("✍️ AI Nhận Diện Chữ Số Viết Tay (MNIST)")

# Tải mô hình đã huấn luyện lên
@st.cache_resource
def load_local_model():
    with open("mnist_model.pkl", 'rb') as f:
        return pickle.load(f)

try:
    model = load_local_model()
except Exception as e:
    st.error("Chưa tìm thấy file 'mnist_model.pkl'. Hãy chạy file train.py trước!")
    st.stop()

# Hàm xử lý hình ảnh chung (Chuyển thành ảnh xám 28x28 và dự đoán)
def predict_digit(pil_image):
    # Chuyển ảnh sang ảnh xám (L) và đổi kích thước về 28x28 pixel
    img_gray = pil_image.convert('L').resize((28, 28))
    
    # Chuyển thành mảng numpy phẳng 784 phần tử và chuẩn hóa
    img_array = np.array(img_gray).astype("float32") / 255.0
    img_flatten = img_array.reshape(1, -1)
    
    # AI dự đoán
    label = model.predict(img_flatten)[0]
    probabilities = model.predict_proba(img_flatten)[0]
    confidence = probabilities[int(label)] * 100
    
    return label, confidence

# Tạo menu lựa chọn tính năng
option = st.radio("Chọn phương thức nhập dữ liệu:", ("Tự tay vẽ số", "Tải ảnh từ máy tính lên"))

# --- THỨ NHẤT: CHỨC NĂNG TỰ VẼ ---
if option == "Tự tay vẽ số":
    st.write("Hãy vẽ một số bất kỳ vào khung dưới đây:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 1)",
        stroke_width=18,
        stroke_color="#FFFFFF",
        background_color="#000000",
        update_streamlit=True,
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        img_data = canvas_result.image_data
        if np.any(img_data[:, :, :3] > 0):
            # Lấy ảnh từ canvas đưa vào hàm xử lý
            raw_img = Image.fromarray(img_data.astype('uint8'))
            label, conf = predict_digit(raw_img)
            st.success(f"### Kết quả vẽ: **{label}** (Độ tin cậy: {conf:.2f}%)")
        else:
            st.info("Hãy vẽ một số để AI nhận diện.")

# --- THỨ HAI: CHỨC NĂNG TẢI ẢNH ---
else:
    st.write("Hãy chọn một file ảnh chữ số (định dạng PNG, JPG hoặc JPEG):")
    uploaded_file = st.file_uploader("Tải ảnh lên tại đây...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Mở ảnh người dùng tải lên
        user_img = Image.open(uploaded_file)
        
        # Hiển thị ảnh gốc cho người dùng xem
        st.image(user_img, caption="Ảnh bạn đã tải lên", width=150)
        
        # Nhấn nút để bắt đầu nhận diện
        if st.button("Bắt đầu nhận diện ảnh"):
            with st.spinner("AI đang quét hình ảnh..."):
                label, conf = predict_digit(user_img)
            st.success(f"### Kết quả phân loại ảnh: **{label}** (Độ tin cậy: {conf:.2f}%)")