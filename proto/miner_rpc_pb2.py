# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: miner_rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="miner_rpc.proto",
    package="index.miner.rpc",
    syntax="proto3",
    serialized_options=b"Z.github.com/textileio/powergate/index/miner/rpc",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0fminer_rpc.proto\x12\x0findex.miner.rpc"_\n\x05Index\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.index.miner.rpc.MetaIndex\x12,\n\x05\x63hain\x18\x02 \x01(\x0b\x32\x1d.index.miner.rpc.OnChainIndex"\xac\x01\n\x0cOnChainIndex\x12\x14\n\x0clast_updated\x18\x01 \x01(\x03\x12\x39\n\x06miners\x18\x02 \x03(\x0b\x32).index.miner.rpc.OnChainIndex.MinersEntry\x1aK\n\x0bMinersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.index.miner.rpc.OnChainData:\x02\x38\x01"_\n\x0bOnChainData\x12\r\n\x05power\x18\x01 \x01(\x04\x12\x16\n\x0erelative_power\x18\x02 \x01(\x02\x12\x13\n\x0bsector_size\x18\x03 \x01(\x04\x12\x14\n\x0c\x61\x63tive_deals\x18\x04 \x01(\x04"\xa4\x01\n\tMetaIndex\x12\x0e\n\x06online\x18\x01 \x01(\r\x12\x0f\n\x07offline\x18\x02 \x01(\r\x12\x32\n\x04info\x18\x03 \x03(\x0b\x32$.index.miner.rpc.MetaIndex.InfoEntry\x1a\x42\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.index.miner.rpc.Meta:\x02\x38\x01"m\n\x04Meta\x12\x14\n\x0clast_updated\x18\x01 \x01(\x03\x12\x12\n\nuser_agent\x18\x02 \x01(\t\x12+\n\x08location\x18\x03 \x01(\x0b\x32\x19.index.miner.rpc.Location\x12\x0e\n\x06online\x18\x04 \x01(\x08"@\n\x08Location\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01"\x0c\n\nGetRequest"4\n\x0bGetResponse\x12%\n\x05index\x18\x01 \x01(\x0b\x32\x16.index.miner.rpc.Index2P\n\nRPCService\x12\x42\n\x03Get\x12\x1b.index.miner.rpc.GetRequest\x1a\x1c.index.miner.rpc.GetResponse"\x00\x42\x30Z.github.com/textileio/powergate/index/miner/rpcb\x06proto3',
)


_INDEX = _descriptor.Descriptor(
    name="Index",
    full_name="index.miner.rpc.Index",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="meta",
            full_name="index.miner.rpc.Index.meta",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="chain",
            full_name="index.miner.rpc.Index.chain",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=36,
    serialized_end=131,
)


_ONCHAININDEX_MINERSENTRY = _descriptor.Descriptor(
    name="MinersEntry",
    full_name="index.miner.rpc.OnChainIndex.MinersEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="index.miner.rpc.OnChainIndex.MinersEntry.key",
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
            name="value",
            full_name="index.miner.rpc.OnChainIndex.MinersEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=231,
    serialized_end=306,
)

_ONCHAININDEX = _descriptor.Descriptor(
    name="OnChainIndex",
    full_name="index.miner.rpc.OnChainIndex",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="last_updated",
            full_name="index.miner.rpc.OnChainIndex.last_updated",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="miners",
            full_name="index.miner.rpc.OnChainIndex.miners",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
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
    nested_types=[
        _ONCHAININDEX_MINERSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=134,
    serialized_end=306,
)


_ONCHAINDATA = _descriptor.Descriptor(
    name="OnChainData",
    full_name="index.miner.rpc.OnChainData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="power",
            full_name="index.miner.rpc.OnChainData.power",
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
        _descriptor.FieldDescriptor(
            name="relative_power",
            full_name="index.miner.rpc.OnChainData.relative_power",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="sector_size",
            full_name="index.miner.rpc.OnChainData.sector_size",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="active_deals",
            full_name="index.miner.rpc.OnChainData.active_deals",
            index=3,
            number=4,
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
    serialized_start=308,
    serialized_end=403,
)


_METAINDEX_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="index.miner.rpc.MetaIndex.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="index.miner.rpc.MetaIndex.InfoEntry.key",
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
            name="value",
            full_name="index.miner.rpc.MetaIndex.InfoEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=504,
    serialized_end=570,
)

_METAINDEX = _descriptor.Descriptor(
    name="MetaIndex",
    full_name="index.miner.rpc.MetaIndex",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="online",
            full_name="index.miner.rpc.MetaIndex.online",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
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
        _descriptor.FieldDescriptor(
            name="offline",
            full_name="index.miner.rpc.MetaIndex.offline",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
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
        _descriptor.FieldDescriptor(
            name="info",
            full_name="index.miner.rpc.MetaIndex.info",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
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
    nested_types=[
        _METAINDEX_INFOENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=406,
    serialized_end=570,
)


_META = _descriptor.Descriptor(
    name="Meta",
    full_name="index.miner.rpc.Meta",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="last_updated",
            full_name="index.miner.rpc.Meta.last_updated",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="user_agent",
            full_name="index.miner.rpc.Meta.user_agent",
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
            name="location",
            full_name="index.miner.rpc.Meta.location",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="online",
            full_name="index.miner.rpc.Meta.online",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=572,
    serialized_end=681,
)


_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="index.miner.rpc.Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="country",
            full_name="index.miner.rpc.Location.country",
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
            name="longitude",
            full_name="index.miner.rpc.Location.longitude",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="latitude",
            full_name="index.miner.rpc.Location.latitude",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_start=683,
    serialized_end=747,
)


_GETREQUEST = _descriptor.Descriptor(
    name="GetRequest",
    full_name="index.miner.rpc.GetRequest",
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
    serialized_start=749,
    serialized_end=761,
)


_GETRESPONSE = _descriptor.Descriptor(
    name="GetResponse",
    full_name="index.miner.rpc.GetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="index.miner.rpc.GetResponse.index",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=763,
    serialized_end=815,
)

_INDEX.fields_by_name["meta"].message_type = _METAINDEX
_INDEX.fields_by_name["chain"].message_type = _ONCHAININDEX
_ONCHAININDEX_MINERSENTRY.fields_by_name["value"].message_type = _ONCHAINDATA
_ONCHAININDEX_MINERSENTRY.containing_type = _ONCHAININDEX
_ONCHAININDEX.fields_by_name["miners"].message_type = _ONCHAININDEX_MINERSENTRY
_METAINDEX_INFOENTRY.fields_by_name["value"].message_type = _META
_METAINDEX_INFOENTRY.containing_type = _METAINDEX
_METAINDEX.fields_by_name["info"].message_type = _METAINDEX_INFOENTRY
_META.fields_by_name["location"].message_type = _LOCATION
_GETRESPONSE.fields_by_name["index"].message_type = _INDEX
DESCRIPTOR.message_types_by_name["Index"] = _INDEX
DESCRIPTOR.message_types_by_name["OnChainIndex"] = _ONCHAININDEX
DESCRIPTOR.message_types_by_name["OnChainData"] = _ONCHAINDATA
DESCRIPTOR.message_types_by_name["MetaIndex"] = _METAINDEX
DESCRIPTOR.message_types_by_name["Meta"] = _META
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
DESCRIPTOR.message_types_by_name["GetRequest"] = _GETREQUEST
DESCRIPTOR.message_types_by_name["GetResponse"] = _GETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Index = _reflection.GeneratedProtocolMessageType(
    "Index",
    (_message.Message,),
    {
        "DESCRIPTOR": _INDEX,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.Index)
    },
)
_sym_db.RegisterMessage(Index)

OnChainIndex = _reflection.GeneratedProtocolMessageType(
    "OnChainIndex",
    (_message.Message,),
    {
        "MinersEntry": _reflection.GeneratedProtocolMessageType(
            "MinersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _ONCHAININDEX_MINERSENTRY,
                "__module__": "miner_rpc_pb2"
                # @@protoc_insertion_point(class_scope:index.miner.rpc.OnChainIndex.MinersEntry)
            },
        ),
        "DESCRIPTOR": _ONCHAININDEX,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.OnChainIndex)
    },
)
_sym_db.RegisterMessage(OnChainIndex)
_sym_db.RegisterMessage(OnChainIndex.MinersEntry)

OnChainData = _reflection.GeneratedProtocolMessageType(
    "OnChainData",
    (_message.Message,),
    {
        "DESCRIPTOR": _ONCHAINDATA,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.OnChainData)
    },
)
_sym_db.RegisterMessage(OnChainData)

MetaIndex = _reflection.GeneratedProtocolMessageType(
    "MetaIndex",
    (_message.Message,),
    {
        "InfoEntry": _reflection.GeneratedProtocolMessageType(
            "InfoEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _METAINDEX_INFOENTRY,
                "__module__": "miner_rpc_pb2"
                # @@protoc_insertion_point(class_scope:index.miner.rpc.MetaIndex.InfoEntry)
            },
        ),
        "DESCRIPTOR": _METAINDEX,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.MetaIndex)
    },
)
_sym_db.RegisterMessage(MetaIndex)
_sym_db.RegisterMessage(MetaIndex.InfoEntry)

Meta = _reflection.GeneratedProtocolMessageType(
    "Meta",
    (_message.Message,),
    {
        "DESCRIPTOR": _META,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.Meta)
    },
)
_sym_db.RegisterMessage(Meta)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATION,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.Location)
    },
)
_sym_db.RegisterMessage(Location)

GetRequest = _reflection.GeneratedProtocolMessageType(
    "GetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREQUEST,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.GetRequest)
    },
)
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType(
    "GetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETRESPONSE,
        "__module__": "miner_rpc_pb2"
        # @@protoc_insertion_point(class_scope:index.miner.rpc.GetResponse)
    },
)
_sym_db.RegisterMessage(GetResponse)


DESCRIPTOR._options = None
_ONCHAININDEX_MINERSENTRY._options = None
_METAINDEX_INFOENTRY._options = None

_RPCSERVICE = _descriptor.ServiceDescriptor(
    name="RPCService",
    full_name="index.miner.rpc.RPCService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=817,
    serialized_end=897,
    methods=[
        _descriptor.MethodDescriptor(
            name="Get",
            full_name="index.miner.rpc.RPCService.Get",
            index=0,
            containing_service=None,
            input_type=_GETREQUEST,
            output_type=_GETRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name["RPCService"] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)
