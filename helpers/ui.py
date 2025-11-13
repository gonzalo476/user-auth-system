from PySide6 import QtWidgets
from typing import List, Any, Optional


class UiHelper:

    @staticmethod
    def get_child_names(
        parent: QtWidgets.QWidget, type: QtWidgets.QLineEdit
    ) -> list[str]:

        widget_list = []

        for widget in parent.findChildren(type):
            name = widget.objectName()
            widget_list.append(name)

        return widget_list

    @staticmethod
    def clear_widgets_message_state(
        parent: QtWidgets.QWidget, list: List, type: QtWidgets.QLineEdit
    ) -> None:

        for widget_name in list:
            widget = parent.findChild(type, widget_name)
            widget.setStyleSheet("")


def clear_qline_widget_messages(parent: QtWidgets.QWidget) -> None:
    widget_list = UiHelper.get_child_names(parent=parent, type=QtWidgets.QLineEdit)
    UiHelper.clear_widgets_message_state(
        parent=parent, list=widget_list, type=QtWidgets.QLineEdit
    )
