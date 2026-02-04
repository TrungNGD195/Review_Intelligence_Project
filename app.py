import streamlit as st

# Thiết lập tiêu đề trang web
st.set_page_config(page_title="Review Intelligence", page_icon="📊")

# Hiện chữ lên màn hình
st.title("Chào mừng đến với dự án Review Intelligence! 🚀")
st.write("Đây là sản phẩm của nhóm chúng tôi.")

# Thử tạo một cái nút bấm
if st.button("Bấm vào tôi đi"):
    st.balloons()  # Hiệu ứng thả bóng bay chúc mừng
    st.success("Bạn đã cài đặt môi trường thành công! Chúc mừng!")