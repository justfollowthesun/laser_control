/****************************************************************************
** Meta object code from reading C++ file '_mainwindow.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../StateSpam/_mainwindow.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file '_mainwindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata__MainWindow_t {
    QByteArrayData data[13];
    char stringdata0[208];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata__MainWindow_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata__MainWindow_t qt_meta_stringdata__MainWindow = {
    {
QT_MOC_LITERAL(0, 0, 11), // "_MainWindow"
QT_MOC_LITERAL(1, 12, 29), // "on_pushButton_Connect_clicked"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 15), // "on_SetConnState"
QT_MOC_LITERAL(4, 59, 2), // "st"
QT_MOC_LITERAL(5, 62, 32), // "on_pushButton_SelectFile_clicked"
QT_MOC_LITERAL(6, 95, 32), // "on_lineEdit_FileName_textChanged"
QT_MOC_LITERAL(7, 128, 4), // "arg1"
QT_MOC_LITERAL(8, 133, 29), // "on_pushButton_RunFile_clicked"
QT_MOC_LITERAL(9, 163, 26), // "on_pushButton_Stop_clicked"
QT_MOC_LITERAL(10, 190, 6), // "on_Log"
QT_MOC_LITERAL(11, 197, 3), // "msg"
QT_MOC_LITERAL(12, 201, 6) // "on_Msg"

    },
    "_MainWindow\0on_pushButton_Connect_clicked\0"
    "\0on_SetConnState\0st\0"
    "on_pushButton_SelectFile_clicked\0"
    "on_lineEdit_FileName_textChanged\0arg1\0"
    "on_pushButton_RunFile_clicked\0"
    "on_pushButton_Stop_clicked\0on_Log\0msg\0"
    "on_Msg"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data__MainWindow[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   54,    2, 0x08 /* Private */,
       3,    1,   55,    2, 0x08 /* Private */,
       5,    0,   58,    2, 0x08 /* Private */,
       6,    1,   59,    2, 0x08 /* Private */,
       8,    0,   62,    2, 0x08 /* Private */,
       9,    0,   63,    2, 0x08 /* Private */,
      10,    1,   64,    2, 0x08 /* Private */,
      12,    1,   67,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    4,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,   11,
    QMetaType::Void, QMetaType::QString,   11,

       0        // eod
};

void _MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<_MainWindow *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->on_pushButton_Connect_clicked(); break;
        case 1: _t->on_SetConnState((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->on_pushButton_SelectFile_clicked(); break;
        case 3: _t->on_lineEdit_FileName_textChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->on_pushButton_RunFile_clicked(); break;
        case 5: _t->on_pushButton_Stop_clicked(); break;
        case 6: _t->on_Log((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 7: _t->on_Msg((*reinterpret_cast< QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject _MainWindow::staticMetaObject = { {
    QMetaObject::SuperData::link<QMainWindow::staticMetaObject>(),
    qt_meta_stringdata__MainWindow.data,
    qt_meta_data__MainWindow,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *_MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *_MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata__MainWindow.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int _MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE