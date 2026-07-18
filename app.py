import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản lý chi tiêu", page_icon="💰")

st.title("💰 QUẢN LÝ CHI TIÊU CÁ NHÂN")

# Khởi tạo dữ liệu
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Tên khoản", "Loại", "Số tiền"])

# Nhập dữ liệu
ten = st.text_input("Tên khoản")
so_tien = st.number_input("Số tiền", min_value=0)
loai = st.radio("Loại", ["Thu", "Chi"])

if st.button("Thêm giao dịch"):
    new_row = pd.DataFrame({
        "Tên khoản": [ten],
        "Loại": [loai],
        "Số tiền": [so_tien]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_row],
        ignore_index=True
    )

st.subheader("📋 Danh sách giao dịch")
st.dataframe(st.session_state.data)

tong_thu = st.session_state.data[
    st.session_state.data["Loại"] == "Thu"
]["Số tiền"].sum()

tong_chi = st.session_state.data[
    st.session_state.data["Loại"] == "Chi"
]["Số tiền"].sum()

so_du = tong_thu - tong_chi

st.metric("💵 Tổng thu", f"{tong_thu:,.0f} VNĐ")
st.metric("💸 Tổng chi", f"{tong_chi:,.0f} VNĐ")
st.metric("💰 Số dư", f"{so_du:,.0f} VNĐ")
