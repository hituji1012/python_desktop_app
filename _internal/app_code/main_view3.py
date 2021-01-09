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
        self.menus = {'File': self.menuBar().addMenu('File'),
                      'Edit': self.menuBar().addMenu('Edit'),
                      'Help': self.menuBar().addMenu('Help'),}

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

        # ------------------ その3ツールバーの設定 --------------------
        # ToolBarを定義
        title = 'Tools'
        self.tools = QToolBar(title)
        self.tools.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # self.addToolBar(Qt.LeftToolBarArea, toolbar) #左に配置
        self.addToolBar(Qt.TopToolBarArea, self.tools) #上に配置

        # ツールバーのアクションを定義
        open_file = new_action(self,
                               text='OpenFile',
                               slot=self.open_file,
                               icon='open',
                               tip='Open File')
        save_file = new_action(self,
                               text='SaveFile',
                               slot=self.save_file,
                               shortcut='Ctrl+S',
                               icon='save',
                               tip='Save File')

        # ツールバーにアクションを追加
        self.tools.clear()
        self.tools.addAction(open_file)
        self.tools.addAction(save_file)

        self.load_data = None


    def show_info(self):
        """ Helpメニュ用メソッド """
        print("desktop app")

    def open_file(self):
        """ ツールバーメソッド """
        fp = QFileDialog.getOpenFileName(self, 'CSV 読込先を選択', "hoge.csv", "CSV (*.csv)")
        if fp[0]:
            with open(fp[0]) as f:
                self.load_data = f.read()
                QMessageBox.information(self, 'ファイル読み込み', '正常に読み込みました。')
                print(self.load_data)

    def save_file(self):
        """ ツールバーメソッド """
        if self.load_data:
            fp = QFileDialog.getSaveFileName(self, 'CSV 保存先を選択', "hoge.csv", "CSV (*.csv)")
            if fp[0]:
                with open(fp[0], mode='w') as f:
                    f.write(self.load_data)
                QMessageBox.information(self, 'ファイル保存', '正常に保存しました。')
        else:
            QMessageBox.critical(self, 'Error Message', 'データ読み込まれていません。')


def get_main_app(argv=[]):
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    return app, win

if __name__ == '__main__':
    app, _win = get_main_app(sys.argv)
    sys.exit(app.exec_())