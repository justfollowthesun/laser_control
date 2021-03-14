/********************************************************************************
** Form generated from reading UI file '_mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI__MAINWINDOW_H
#define UI__MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui__MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout_4;
    QVBoxLayout *verticalLayout_2;
    QListWidget *listWidget_sent;
    QListWidget *listWidget_Log;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton_Connect;
    QSpinBox *spinBox_Port;
    QHBoxLayout *horizontalLayout_2;
    QLineEdit *lineEdit_FileName;
    QPushButton *pushButton_SelectFile;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *pushButton_RunFile;
    QSpinBox *spinBox_Freq;
    QPushButton *pushButton_Stop;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *_MainWindow)
    {
        if (_MainWindow->objectName().isEmpty())
            _MainWindow->setObjectName(QString::fromUtf8("_MainWindow"));
        _MainWindow->resize(811, 613);
        centralwidget = new QWidget(_MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout_4 = new QHBoxLayout(centralwidget);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        listWidget_sent = new QListWidget(centralwidget);
        listWidget_sent->setObjectName(QString::fromUtf8("listWidget_sent"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(3);
        sizePolicy.setHeightForWidth(listWidget_sent->sizePolicy().hasHeightForWidth());
        listWidget_sent->setSizePolicy(sizePolicy);

        verticalLayout_2->addWidget(listWidget_sent);

        listWidget_Log = new QListWidget(centralwidget);
        listWidget_Log->setObjectName(QString::fromUtf8("listWidget_Log"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(1);
        sizePolicy1.setHeightForWidth(listWidget_Log->sizePolicy().hasHeightForWidth());
        listWidget_Log->setSizePolicy(sizePolicy1);

        verticalLayout_2->addWidget(listWidget_Log);


        horizontalLayout_4->addLayout(verticalLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        pushButton_Connect = new QPushButton(centralwidget);
        pushButton_Connect->setObjectName(QString::fromUtf8("pushButton_Connect"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(pushButton_Connect->sizePolicy().hasHeightForWidth());
        pushButton_Connect->setSizePolicy(sizePolicy2);

        horizontalLayout->addWidget(pushButton_Connect);

        spinBox_Port = new QSpinBox(centralwidget);
        spinBox_Port->setObjectName(QString::fromUtf8("spinBox_Port"));
        sizePolicy2.setHeightForWidth(spinBox_Port->sizePolicy().hasHeightForWidth());
        spinBox_Port->setSizePolicy(sizePolicy2);
        spinBox_Port->setMaximum(65536);
        spinBox_Port->setValue(12345);

        horizontalLayout->addWidget(spinBox_Port);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        lineEdit_FileName = new QLineEdit(centralwidget);
        lineEdit_FileName->setObjectName(QString::fromUtf8("lineEdit_FileName"));
        sizePolicy2.setHeightForWidth(lineEdit_FileName->sizePolicy().hasHeightForWidth());
        lineEdit_FileName->setSizePolicy(sizePolicy2);

        horizontalLayout_2->addWidget(lineEdit_FileName);

        pushButton_SelectFile = new QPushButton(centralwidget);
        pushButton_SelectFile->setObjectName(QString::fromUtf8("pushButton_SelectFile"));
        QSizePolicy sizePolicy3(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(pushButton_SelectFile->sizePolicy().hasHeightForWidth());
        pushButton_SelectFile->setSizePolicy(sizePolicy3);
        pushButton_SelectFile->setMaximumSize(QSize(25, 16777215));

        horizontalLayout_2->addWidget(pushButton_SelectFile);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        pushButton_RunFile = new QPushButton(centralwidget);
        pushButton_RunFile->setObjectName(QString::fromUtf8("pushButton_RunFile"));
        sizePolicy2.setHeightForWidth(pushButton_RunFile->sizePolicy().hasHeightForWidth());
        pushButton_RunFile->setSizePolicy(sizePolicy2);

        horizontalLayout_3->addWidget(pushButton_RunFile);

        spinBox_Freq = new QSpinBox(centralwidget);
        spinBox_Freq->setObjectName(QString::fromUtf8("spinBox_Freq"));
        sizePolicy2.setHeightForWidth(spinBox_Freq->sizePolicy().hasHeightForWidth());
        spinBox_Freq->setSizePolicy(sizePolicy2);
        spinBox_Freq->setValue(99);

        horizontalLayout_3->addWidget(spinBox_Freq);


        verticalLayout->addLayout(horizontalLayout_3);

        pushButton_Stop = new QPushButton(centralwidget);
        pushButton_Stop->setObjectName(QString::fromUtf8("pushButton_Stop"));
        QSizePolicy sizePolicy4(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(pushButton_Stop->sizePolicy().hasHeightForWidth());
        pushButton_Stop->setSizePolicy(sizePolicy4);
        pushButton_Stop->setMinimumSize(QSize(250, 0));

        verticalLayout->addWidget(pushButton_Stop);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        horizontalLayout_4->addLayout(verticalLayout);

        _MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(_MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 811, 22));
        _MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(_MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        _MainWindow->setStatusBar(statusbar);

        retranslateUi(_MainWindow);

        QMetaObject::connectSlotsByName(_MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *_MainWindow)
    {
        _MainWindow->setWindowTitle(QCoreApplication::translate("_MainWindow", "State spammer", nullptr));
        pushButton_Connect->setText(QCoreApplication::translate("_MainWindow", "Connect", nullptr));
        lineEdit_FileName->setText(QCoreApplication::translate("_MainWindow", "C:/1.txt", nullptr));
        pushButton_SelectFile->setText(QCoreApplication::translate("_MainWindow", "V", nullptr));
        pushButton_RunFile->setText(QCoreApplication::translate("_MainWindow", "RunFile", nullptr));
        pushButton_Stop->setText(QCoreApplication::translate("_MainWindow", "Stop", nullptr));
    } // retranslateUi

};

namespace Ui {
    class _MainWindow: public Ui__MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI__MAINWINDOW_H
