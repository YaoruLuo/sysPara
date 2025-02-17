import streamlit as st
from dataTree import drive_data
from css import add_custom_styles
from menu import create_menu


# # 添加自定义CSS样式
st.markdown(add_custom_styles(), unsafe_allow_html=True)

# 页面标题和说明
st.markdown(
    "<h1 style='color: #009999; text-align: left;'>SIEMENS 产品参数查询系统</h1>",
    unsafe_allow_html=True,
)

tab_drive, tab_plc, tab_HMI = st.tabs(["SINAMICS驱动", "PLC", "HMI"])

with tab_drive:
    with st.container(border=True):
        st.markdown(
            "<h3 style='color: #009999; text-align: left;'>SINAMICS系列驱动概览</h3>",
            unsafe_allow_html=True
        )

        st.image("./data/driver/sinamics/driver_category_1.png", use_container_width=True)


    with st.container(border=True):
        st.markdown(
            "<h3 style='color: #009999; text-align: left;'>驱动参数查询</h3>",
            unsafe_allow_html=True
        )
        results = create_menu(drive_data)
        query_button_clicked = st.button("查询")

        if query_button_clicked:
            st.markdown("""
                <div class="结果">
                    <h3>查询结果</h3>
                </div>
                """, unsafe_allow_html=True
            )
            for item in results:
                field_name = item[0]
                field_value = item[1]
                if field_name == "imgPath":
                    st.image(field_value, use_container_width=True)
                elif field_name == "link":
                    link_name, link_value = field_value[0], field_value[1]
                    st.markdown(f"点击查看 [{link_name}]({link_value})")
                else:
                    st.write("未找到图片或文档链接")

with tab_plc:
    st.markdown(
        "<h3 style='color: #009999; text-align: left;'>Coming soon...</h3>",
        unsafe_allow_html=True
    )


with tab_HMI:
    st.markdown(
        "<h3 style='color: #009999; text-align: left;'>Coming soon...</h3>",
        unsafe_allow_html=True
    )
