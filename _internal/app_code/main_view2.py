from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


def new_action(parent, text, slot=None, shortcut=None, icon=None, tip=None, enabled=True):
    """actionの設定と取得"""
    # アクション取得
    a = QAction(text, parent)
    # icon設定 iconsフォルダから取得
    if icon is not None:
        a.setIcon(QIcon('icons/'+icon))
    # ショートカット作成
    if shortcut is not None:
        if isinstance(shortcut, (list, tuple)):
            a.setShortcuts(shortcut)
        else:
            a.setShortcut(shortcut)
    # ステータスバーに表示するTip
    if tip is not None:
        a.setToolTip(tip)
        a.setStatusTip(tip)
    # 押したときの動作
    if slot is not None:
        a.triggered.connect(slot)
    # ロックするか
    a.setEnabled(enabled)
    return a


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.resize(QSize(600, 500))
        self.setWindowTitle('app')

        # ------------------ その2メニューの追加 --------------------
        # メニューの追加
        self.menus = {'File': self.menuBar().addMenu('&File'),
                      'Edit': self.menuBar().addMenu('&Edit'),
                      'Help': self.menuBar().addMenu('&Help'),}

        # アクションを設定する
        quit = new_action(self,
                          text='quit',
                          slot=self.close,
                          shortcut='Ctrl+Q',
                          icon='quit',
                          tip='quitApp')
        show_info = new_action(self,
                               text='information',
                               slot=self.show_info,
                               tip='show app information')
        self.menus['File'].addAction(quit)
        self.menus['Help'].addAction(show_info)

        # ステータスバー
        self.statusBar()

    def show_info(self):
        """ Helpメニュ用メソッド """
        print("desktop app")


def get_main_app(argv=[]):
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    return app, win

if __name__ == '__main__':
    app, _win = get_main_app(sys.argv)
    sys.exit(app.exec_())