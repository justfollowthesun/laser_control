/****************************************************************************
** Meta object code from reading C++ file 'TcpConnection.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../StateSpam/TcpConnection.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TcpConnection.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_CTcpConnection_t {
    QByteArrayData data[10];
    char stringdata0[114];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_CTcpConnection_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_CTcpConnection_t qt_meta_stringdata_CTcpConnection = {
    {
QT_MOC_LITERAL(0, 0, 14), // "CTcpConnection"
QT_MOC_LITERAL(1, 15, 16), // "sig_Disconnected"
QT_MOC_LITERAL(2, 32, 0), // ""
QT_MOC_LITERAL(3, 33, 9), // "sig_Error"
QT_MOC_LITERAL(4, 43, 4), // "a_id"
QT_MOC_LITERAL(5, 48, 10), // "a_nErrCode"
QT_MOC_LITERAL(6, 59, 9), // "a_sErrTxt"
QT_MOC_LITERAL(7, 69, 13), // "sig_Connected"
QT_MOC_LITERAL(8, 83, 14), // "on_ReadyToRead"
QT_MOC_LITERAL(9, 98, 15) // "on_Disconnected"

    },
    "CTcpConnection\0sig_Disconnected\0\0"
    "sig_Error\0a_id\0a_nErrCode\0a_sErrTxt\0"
    "sig_Connected\0on_ReadyToRead\0"
    "on_Disconnected"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_CTcpConnection[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   39,    2, 0x06 /* Public */,
       3,    3,   40,    2, 0x06 /* Public */,
       7,    0,   47,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       8,    0,   48,    2, 0x09 /* Protected */,
       9,    0,   49,    2, 0x09 /* Protected */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::ULongLong, QMetaType::ULongLong, QMetaType::QString,    4,    5,    6,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void CTcpConnection::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CTcpConnection *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->sig_Disconnected(); break;
        case 1: _t->sig_Error((*reinterpret_cast< quint64(*)>(_a[1])),(*reinterpret_cast< quint64(*)>(_a[2])),(*reinterpret_cast< QString(*)>(_a[3]))); break;
        case 2: _t->sig_Connected(); break;
        case 3: _t->on_ReadyToRead(); break;
        case 4: _t->on_Disconnected(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CTcpConnection::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpConnection::sig_Disconnected)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CTcpConnection::*)(quint64 , quint64 , QString );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpConnection::sig_Error)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CTcpConnection::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpConnection::sig_Connected)) {
                *result = 2;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject CTcpConnection::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_meta_stringdata_CTcpConnection.data,
    qt_meta_data_CTcpConnection,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *CTcpConnection::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CTcpConnection::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CTcpConnection.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int CTcpConnection::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void CTcpConnection::sig_Disconnected()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void CTcpConnection::sig_Error(quint64 _t1, quint64 _t2, QString _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t3))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void CTcpConnection::sig_Connected()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
