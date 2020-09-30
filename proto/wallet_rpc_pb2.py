# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet_rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="wallet_rpc.proto",
    package="wallet.rpc",
    syntax="proto3",
    serialized_options=b"Z)github.com/textileio/powergate/wallet/rpc",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x10wallet_rpc.proto\x12\nwallet.rpc"!\n\x11NewAddressRequest\x12\x0c\n\x04type\x18\x01 \x01(\t"%\n\x12NewAddressResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t"\x1b\n\x0bListRequest\x12\x0c\n\x04type\x18\x01 \x01(\t"!\n\x0cListResponse\x12\x11\n\taddresses\x18\x01 \x03(\t"!\n\x0e\x42\x61lanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t""\n\x0f\x42\x61lanceResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04":\n\x0eSendFilRequest\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03"\x11\n\x0fSendFilResponse2\xa4\x02\n\nRPCService\x12M\n\nNewAddress\x12\x1d.wallet.rpc.NewAddressRequest\x1a\x1e.wallet.rpc.NewAddressResponse"\x00\x12;\n\x04List\x12\x17.wallet.rpc.ListRequest\x1a\x18.wallet.rpc.ListResponse"\x00\x12\x44\n\x07\x42\x61lance\x12\x1a.wallet.rpc.BalanceRequest\x1a\x1b.wallet.rpc.BalanceResponse"\x00\x12\x44\n\x07SendFil\x12\x1a.wallet.rpc.SendFilRequest\x1a\x1b.wallet.rpc.SendFilResponse"\x00\x42+Z)github.com/textileio/powergate/wallet/rpcb\x06proto3',
)


_NEWADDRESSREQUEST = _descriptor.Descriptor(
    name="NewAddressRequest",
    full_name="wallet.rpc.NewAddressRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="wallet.rpc.NewAddressRequest.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=32,
    serialized_end=65,
)


_NEWADDRESSRESPONSE = _descriptor.Descriptor(
    name="NewAddressResponse",
    full_name="wallet.rpc.NewAddressResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="address",
            full_name="wallet.rpc.NewAddressResponse.address",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=67,
    serialized_end=104,
)


_LISTREQUEST = _descriptor.Descriptor(
    name="ListRequest",
    full_name="wallet.rpc.ListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="wallet.rpc.ListRequest.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=106,
    serialized_end=133,
)


_LISTRESPONSE = _descriptor.Descriptor(
    name="ListResponse",
    full_name="wallet.rpc.ListResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="addresses",
            full_name="wallet.rpc.ListResponse.addresses",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=135,
    serialized_end=168,
)


_BALANCEREQUEST = _descriptor.Descriptor(
    name="BalanceRequest",
    full_name="wallet.rpc.BalanceRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="address",
            full_name="wallet.rpc.BalanceRequest.address",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=170,
    serialized_end=203,
)


_BALANCERESPONSE = _descriptor.Descriptor(
    name="BalanceResponse",
    full_name="wallet.rpc.BalanceResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="balance",
            full_name="wallet.rpc.BalanceResponse.balance",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=205,
    serialized_end=239,
)


_SENDFILREQUEST = _descriptor.Descriptor(
    name="SendFilRequest",
    full_name="wallet.rpc.SendFilRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="from",
            full_name="wallet.rpc.SendFilRequest.from",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="to",
            full_name="wallet.rpc.SendFilRequest.to",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="wallet.rpc.SendFilRequest.amount",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=241,
    serialized_end=299,
)


_SENDFILRESPONSE = _descriptor.Descriptor(
    name="SendFilResponse",
    full_name="wallet.rpc.SendFilResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=301,
    serialized_end=318,
)

DESCRIPTOR.message_types_by_name["NewAddressRequest"] = _NEWADDRESSREQUEST
DESCRIPTOR.message_types_by_name["NewAddressResponse"] = _NEWADDRESSRESPONSE
DESCRIPTOR.message_types_by_name["ListRequest"] = _LISTREQUEST
DESCRIPTOR.message_types_by_name["ListResponse"] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name["BalanceRequest"] = _BALANCEREQUEST
DESCRIPTOR.message_types_by_name["BalanceResponse"] = _BALANCERESPONSE
DESCRIPTOR.message_types_by_name["SendFilRequest"] = _SENDFILREQUEST
DESCRIPTOR.message_types_by_name["SendFilResponse"] = _SENDFILRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewAddressRequest = _reflection.GeneratedProtocolMessageType(
    "NewAddressRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _NEWADDRESSREQUEST,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.NewAddressRequest)
    },
)
_sym_db.RegisterMessage(NewAddressRequest)

NewAddressResponse = _reflection.GeneratedProtocolMessageType(
    "NewAddressResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _NEWADDRESSRESPONSE,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.NewAddressResponse)
    },
)
_sym_db.RegisterMessage(NewAddressResponse)

ListRequest = _reflection.GeneratedProtocolMessageType(
    "ListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTREQUEST,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.ListRequest)
    },
)
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType(
    "ListResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTRESPONSE,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.ListResponse)
    },
)
_sym_db.RegisterMessage(ListResponse)

BalanceRequest = _reflection.GeneratedProtocolMessageType(
    "BalanceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BALANCEREQUEST,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.BalanceRequest)
    },
)
_sym_db.RegisterMessage(BalanceRequest)

BalanceResponse = _reflection.GeneratedProtocolMessageType(
    "BalanceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BALANCERESPONSE,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.BalanceResponse)
    },
)
_sym_db.RegisterMessage(BalanceResponse)

SendFilRequest = _reflection.GeneratedProtocolMessageType(
    "SendFilRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDFILREQUEST,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.SendFilRequest)
    },
)
_sym_db.RegisterMessage(SendFilRequest)

SendFilResponse = _reflection.GeneratedProtocolMessageType(
    "SendFilResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDFILRESPONSE,
        "__module__": "wallet_rpc_pb2"
        # @@protoc_insertion_point(class_scope:wallet.rpc.SendFilResponse)
    },
)
_sym_db.RegisterMessage(SendFilResponse)


DESCRIPTOR._options = None

_RPCSERVICE = _descriptor.ServiceDescriptor(
    name="RPCService",
    full_name="wallet.rpc.RPCService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=321,
    serialized_end=613,
    methods=[
        _descriptor.MethodDescriptor(
            name="NewAddress",
            full_name="wallet.rpc.RPCService.NewAddress",
            index=0,
            containing_service=None,
            input_type=_NEWADDRESSREQUEST,
            output_type=_NEWADDRESSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="List",
            full_name="wallet.rpc.RPCService.List",
            index=1,
            containing_service=None,
            input_type=_LISTREQUEST,
            output_type=_LISTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Balance",
            full_name="wallet.rpc.RPCService.Balance",
            index=2,
            containing_service=None,
            input_type=_BALANCEREQUEST,
            output_type=_BALANCERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendFil",
            full_name="wallet.rpc.RPCService.SendFil",
            index=3,
            containing_service=None,
            input_type=_SENDFILREQUEST,
            output_type=_SENDFILRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name["RPCService"] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)
