/****************************************************************************
** Meta object code from reading C++ file 'TcpClient.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../StateSpam/TcpClient.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TcpClient.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_CTcpClient_t {
    QByteArrayData data[21];
    char stringdata0[221];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_CTcpClient_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_CTcpClient_t qt_meta_stringdata_CTcpClient = {
    {
QT_MOC_LITERAL(0, 0, 10), // "CTcpClient"
QT_MOC_LITERAL(1, 11, 9), // "sig_Start"
QT_MOC_LITERAL(2, 21, 0), // ""
QT_MOC_LITERAL(3, 22, 7), // "a_nPort"
QT_MOC_LITERAL(4, 30, 7), // "a_sHost"
QT_MOC_LITERAL(5, 38, 11), // "sig_SendMsg"
QT_MOC_LITERAL(6, 50, 6), // "a_sMsg"
QT_MOC_LITERAL(7, 57, 8), // "sig_Stop"
QT_MOC_LITERAL(8, 66, 13), // "sig_Connected"
QT_MOC_LITERAL(9, 80, 19), // "sig_MessageReceived"
QT_MOC_LITERAL(10, 100, 4), // "a_id"
QT_MOC_LITERAL(11, 105, 11), // "sig_Timeout"
QT_MOC_LITERAL(12, 117, 16), // "sig_Disconnected"
QT_MOC_LITERAL(13, 134, 9), // "sig_Error"
QT_MOC_LITERAL(14, 144, 10), // "a_nErrCode"
QT_MOC_LITERAL(15, 155, 9), // "a_sErrTxt"
QT_MOC_LITERAL(16, 165, 8), // "on_Start"
QT_MOC_LITERAL(17, 174, 18), // "on_MessageReceived"
QT_MOC_LITERAL(18, 193, 8), // "on_Error"
QT_MOC_LITERAL(19, 202, 10), // "a_sErrCode"
QT_MOC_LITERAL(20, 213, 7) // "on_Stop"

    },
    "CTcpClient\0sig_Start\0\0a_nPort\0a_sHost\0"
    "sig_SendMsg\0a_sMsg\0sig_Stop\0sig_Connected\0"
    "sig_MessageReceived\0a_id\0sig_Timeout\0"
    "sig_Disconnected\0sig_Error\0a_nErrCode\0"
    "a_sErrTxt\0on_Start\0on_MessageReceived\0"
    "on_Error\0a_sErrCode\0on_Stop"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_CTcpClient[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       8,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,   74,    2, 0x06 /* Public */,
       5,    1,   79,    2, 0x06 /* Public */,
       7,    0,   82,    2, 0x06 /* Public */,
       8,    0,   83,    2, 0x06 /* Public */,
       9,    2,   84,    2, 0x06 /* Public */,
      11,    1,   89,    2, 0x06 /* Public */,
      12,    0,   92,    2, 0x06 /* Public */,
      13,    3,   93,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      16,    2,  100,    2, 0x08 /* Private */,
      17,    2,  105,    2, 0x08 /* Private */,
      18,    3,  110,    2, 0x08 /* Private */,
      20,    0,  117,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::UShort, QMetaType::QString,    3,    4,
    QMetaType::Void, QMetaType::QString,    6,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString, QMetaType::ULongLong,    6,   10,
    QMetaType::Void, QMetaType::ULongLong,   10,
    QMetaType::Void,
    QMetaType::Void, QMetaType::ULongLong, QMetaType::ULongLong, QMetaType::QString,   10,   14,   15,

 // slots: parameters
    QMetaType::Void, QMetaType::UShort, QMetaType::QString,    3,    4,
    QMetaType::Void, QMetaType::QString, QMetaType::ULongLong,    6,   10,
    QMetaType::Void, QMetaType::ULongLong, QMetaType::ULongLong, QMetaType::QString,   10,   19,    6,
    QMetaType::Void,

       0        // eod
};

void CTcpClient::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CTcpClient *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->sig_Start((*reinterpret_cast< quint16(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2])), QPrivateSignal()); break;
        case 1: _t->sig_SendMsg((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 2: _t->sig_Stop(QPrivateSignal()); break;
        case 3: _t->sig_Connected(); break;
        case 4: _t->sig_MessageReceived((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< quint64(*)>(_a[2]))); break;
        case 5: _t->sig_Timeout((*reinterpret_cast< quint64(*)>(_a[1]))); break;
        case 6: _t->sig_Disconnected(); break;
        case 7: _t->sig_Error((*reinterpret_cast< quint64(*)>(_a[1])),(*reinterpret_cast< quint64(*)>(_a[2])),(*reinterpret_cast< QString(*)>(_a[3]))); break;
        case 8: _t->on_Start((*reinterpret_cast< quint16(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 9: _t->on_MessageReceived((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< quint64(*)>(_a[2]))); break;
        case 10: _t->on_Error((*reinterpret_cast< quint64(*)>(_a[1])),(*reinterpret_cast< quint64(*)>(_a[2])),(*reinterpret_cast< QString(*)>(_a[3]))); break;
        case 11: _t->on_Stop(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CTcpClient::*)(quint16 , const QString & , QPrivateSignal);
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Start)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)(QString );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_SendMsg)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)(QPrivateSignal);
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Stop)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Connected)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)(QString , quint64 );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_MessageReceived)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)(quint64 );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Timeout)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Disconnected)) {
                *result = 6;
                return;
            }
        }
        {
            using _t = void (CTcpClient::*)(quint64 , quint64 , QString );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CTcpClient::sig_Error)) {
                *result = 7;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject CTcpClient::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_meta_stringdata_CTcpClient.data,
    qt_meta_data_CTcpClient,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *CTcpClient::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CTcpClient::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CTcpClient.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int CTcpClient::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 12)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 12)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 12;
    }
    return _id;
}

// SIGNAL 0
void CTcpClient::sig_Start(quint16 _t1, const QString & _t2, QPrivateSignal _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t3))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void CTcpClient::sig_SendMsg(QString _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void CTcpClient::sig_Stop(QPrivateSignal _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void CTcpClient::sig_Connected()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void CTcpClient::sig_MessageReceived(QString _t1, quint64 _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void CTcpClient::sig_Timeout(quint64 _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void CTcpClient::sig_Disconnected()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void CTcpClient::sig_Error(quint64 _t1, quint64 _t2, QString _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t3))) };
    QMetaObject::activate(this, &staticMetaObject, 7, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
