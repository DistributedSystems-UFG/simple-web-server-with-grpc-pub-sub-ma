from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Dado(_message.Message):
    __slots__ = ["data", "id", "localizacao", "valor"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZACAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    data: str
    id: int
    localizacao: str
    valor: float
    def __init__(self, id: _Optional[int] = ..., data: _Optional[str] = ..., localizacao: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListaDados(_message.Message):
    __slots__ = ["dados"]
    DADOS_FIELD_NUMBER: _ClassVar[int]
    dados: _containers.RepeatedCompositeFieldContainer[Dado]
    def __init__(self, dados: _Optional[_Iterable[_Union[Dado, _Mapping]]] = ...) -> None: ...

class LocalData(_message.Message):
    __slots__ = ["data", "local"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    data: Data
    local: Localizacao
    def __init__(self, local: _Optional[_Union[Localizacao, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class Localizacao(_message.Message):
    __slots__ = ["localizacao"]
    LOCALIZACAO_FIELD_NUMBER: _ClassVar[int]
    localizacao: str
    def __init__(self, localizacao: _Optional[str] = ...) -> None: ...
