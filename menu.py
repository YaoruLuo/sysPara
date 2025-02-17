# menu_generator.py

import streamlit as st


def create_menu(data, level=1):
    """根据当前的数据和层级生成菜单"""
    # 获取当前数据的键作为菜单选项
    keys = list(data.keys())
    if not keys:
        return None

    # 在当前层级生成按钮
    menu_option = st.selectbox(f"第{level}层菜单", keys, key=f"level_{level}")

    # 获取用户选择后，获取该选项的数据
    selected_item = data[menu_option]

    # 如果选中的项目是字典，表示还有子菜单，递归生成下一层级的菜单
    if isinstance(selected_item, dict):
        # 递归调用生成下一层级的菜单
        return create_menu(selected_item, level + 1)
    else:
        # 如果是最终选项，直接返回选中的项
        return selected_item


