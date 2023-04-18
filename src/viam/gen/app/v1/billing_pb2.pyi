"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CurrentMonthUsageSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLOUD_STORAGE_USAGE_FIELD_NUMBER: builtins.int
    CLOUD_STORAGE_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_UPLOAD_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_UPLOAD_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    DATA_EGRES_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_EGRES_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    STANDARD_COMPUTE_USAGE_COST_FIELD_NUMBER: builtins.int
    STANDARD_COMPUTE_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITH_DISCOUNT_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITHOUT_DISCOUNT_FIELD_NUMBER: builtins.int
    cloud_storage_usage: builtins.float
    cloud_storage_usage_cost: builtins.float
    data_upload_usage_cost: builtins.float
    data_upload_usage_quantity: builtins.float
    data_egres_usage_cost: builtins.float
    data_egres_usage_quantity: builtins.float
    standard_compute_usage_cost: builtins.float
    standard_compute_usage_quantity: builtins.float
    total_usage_quantity: builtins.float
    total_usage_with_discount: builtins.float
    'returns amt with any discounts applied'
    total_usage_without_discount: builtins.float
    'returns amt without any discounts applied'

    def __init__(self, *, cloud_storage_usage: builtins.float=..., cloud_storage_usage_cost: builtins.float=..., data_upload_usage_cost: builtins.float=..., data_upload_usage_quantity: builtins.float=..., data_egres_usage_cost: builtins.float=..., data_egres_usage_quantity: builtins.float=..., standard_compute_usage_cost: builtins.float=..., standard_compute_usage_quantity: builtins.float=..., total_usage_quantity: builtins.float=..., total_usage_with_discount: builtins.float=..., total_usage_without_discount: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['cloud_storage_usage', b'cloud_storage_usage', 'cloud_storage_usage_cost', b'cloud_storage_usage_cost', 'data_egres_usage_cost', b'data_egres_usage_cost', 'data_egres_usage_quantity', b'data_egres_usage_quantity', 'data_upload_usage_cost', b'data_upload_usage_cost', 'data_upload_usage_quantity', b'data_upload_usage_quantity', 'standard_compute_usage_cost', b'standard_compute_usage_cost', 'standard_compute_usage_quantity', b'standard_compute_usage_quantity', 'total_usage_quantity', b'total_usage_quantity', 'total_usage_with_discount', b'total_usage_with_discount', 'total_usage_without_discount', b'total_usage_without_discount']) -> None:
        ...
global___CurrentMonthUsageSummary = CurrentMonthUsageSummary

@typing_extensions.final
class InvoiceSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    INVOICE_DATE_FIELD_NUMBER: builtins.int
    INVOICE_AMOUNT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DUE_DATE_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def invoice_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    invoice_amount: builtins.float
    status: builtins.str

    @property
    def due_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, id: builtins.str=..., invoice_date: google.protobuf.timestamp_pb2.Timestamp | None=..., invoice_amount: builtins.float=..., status: builtins.str=..., due_date: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['due_date', b'due_date', 'invoice_date', b'invoice_date']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['due_date', b'due_date', 'id', b'id', 'invoice_amount', b'invoice_amount', 'invoice_date', b'invoice_date', 'status', b'status']) -> None:
        ...
global___InvoiceSummary = InvoiceSummary

@typing_extensions.final
class BillableResourceEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    USAGE_QUANTITY_UNIT_FIELD_NUMBER: builtins.int
    USAGE_COST_FIELD_NUMBER: builtins.int
    OCCURRED_AT_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    type: builtins.str
    usage_quantity: builtins.float
    usage_quantity_unit: builtins.str
    usage_cost: builtins.str

    @property
    def occurred_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    user_name: builtins.str

    def __init__(self, *, id: builtins.str=..., type: builtins.str=..., usage_quantity: builtins.float=..., usage_quantity_unit: builtins.str=..., usage_cost: builtins.str=..., occurred_at: google.protobuf.timestamp_pb2.Timestamp | None=..., user_name: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['occurred_at', b'occurred_at']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'occurred_at', b'occurred_at', 'type', b'type', 'usage_cost', b'usage_cost', 'usage_quantity', b'usage_quantity', 'usage_quantity_unit', b'usage_quantity_unit', 'user_name', b'user_name']) -> None:
        ...
global___BillableResourceEvent = BillableResourceEvent

@typing_extensions.final
class Invoice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    INVOICE_DATE_FIELD_NUMBER: builtins.int
    INVOICE_AMOUNT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DUE_DATE_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    EMAILED_TO_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def invoice_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    invoice_amount: builtins.float
    status: builtins.str

    @property
    def due_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BillableResourceEvent]:
        ...
    emailed_to: builtins.str

    def __init__(self, *, id: builtins.str=..., invoice_date: google.protobuf.timestamp_pb2.Timestamp | None=..., invoice_amount: builtins.float=..., status: builtins.str=..., due_date: google.protobuf.timestamp_pb2.Timestamp | None=..., items: collections.abc.Iterable[global___BillableResourceEvent] | None=..., emailed_to: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['due_date', b'due_date', 'invoice_date', b'invoice_date']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['due_date', b'due_date', 'emailed_to', b'emailed_to', 'id', b'id', 'invoice_amount', b'invoice_amount', 'invoice_date', b'invoice_date', 'items', b'items', 'status', b'status']) -> None:
        ...
global___Invoice = Invoice

@typing_extensions.final
class GetCurrentMonthUsageSummaryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['org_id', b'org_id']) -> None:
        ...
global___GetCurrentMonthUsageSummaryRequest = GetCurrentMonthUsageSummaryRequest

@typing_extensions.final
class GetCurrentMonthUsageSummaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLOUD_STORAGE_USAGE_FIELD_NUMBER: builtins.int
    CLOUD_STORAGE_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_UPLOAD_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_UPLOAD_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    DATA_EGRES_USAGE_COST_FIELD_NUMBER: builtins.int
    DATA_EGRES_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    STANDARD_COMPUTE_USAGE_COST_FIELD_NUMBER: builtins.int
    STANDARD_COMPUTE_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_QUANTITY_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITH_DISCOUNT_FIELD_NUMBER: builtins.int
    TOTAL_USAGE_WITHOUT_DISCOUNT_FIELD_NUMBER: builtins.int
    cloud_storage_usage: builtins.float
    cloud_storage_usage_cost: builtins.float
    data_upload_usage_cost: builtins.float
    data_upload_usage_quantity: builtins.float
    data_egres_usage_cost: builtins.float
    data_egres_usage_quantity: builtins.float
    standard_compute_usage_cost: builtins.float
    standard_compute_usage_quantity: builtins.float
    total_usage_quantity: builtins.float
    total_usage_with_discount: builtins.float
    'returns amt with any discounts applied'
    total_usage_without_discount: builtins.float
    'returns amt without any discounts applied'

    def __init__(self, *, cloud_storage_usage: builtins.float=..., cloud_storage_usage_cost: builtins.float=..., data_upload_usage_cost: builtins.float=..., data_upload_usage_quantity: builtins.float=..., data_egres_usage_cost: builtins.float=..., data_egres_usage_quantity: builtins.float=..., standard_compute_usage_cost: builtins.float=..., standard_compute_usage_quantity: builtins.float=..., total_usage_quantity: builtins.float=..., total_usage_with_discount: builtins.float=..., total_usage_without_discount: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['cloud_storage_usage', b'cloud_storage_usage', 'cloud_storage_usage_cost', b'cloud_storage_usage_cost', 'data_egres_usage_cost', b'data_egres_usage_cost', 'data_egres_usage_quantity', b'data_egres_usage_quantity', 'data_upload_usage_cost', b'data_upload_usage_cost', 'data_upload_usage_quantity', b'data_upload_usage_quantity', 'standard_compute_usage_cost', b'standard_compute_usage_cost', 'standard_compute_usage_quantity', b'standard_compute_usage_quantity', 'total_usage_quantity', b'total_usage_quantity', 'total_usage_with_discount', b'total_usage_with_discount', 'total_usage_without_discount', b'total_usage_without_discount']) -> None:
        ...
global___GetCurrentMonthUsageSummaryResponse = GetCurrentMonthUsageSummaryResponse

@typing_extensions.final
class GetUnpaidBalanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['org_id', b'org_id']) -> None:
        ...
global___GetUnpaidBalanceRequest = GetUnpaidBalanceRequest

@typing_extensions.final
class GetUnpaidBalanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UNPAID_BALANCE_FIELD_NUMBER: builtins.int
    UNPAID_BALANCE_DUE_DATE_FIELD_NUMBER: builtins.int
    unpaid_balance: builtins.float

    @property
    def unpaid_balance_due_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, unpaid_balance: builtins.float=..., unpaid_balance_due_date: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['unpaid_balance_due_date', b'unpaid_balance_due_date']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['unpaid_balance', b'unpaid_balance', 'unpaid_balance_due_date', b'unpaid_balance_due_date']) -> None:
        ...
global___GetUnpaidBalanceResponse = GetUnpaidBalanceResponse

@typing_extensions.final
class GetInvoiceHistoryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['org_id', b'org_id']) -> None:
        ...
global___GetInvoiceHistoryRequest = GetInvoiceHistoryRequest

@typing_extensions.final
class GetInvoiceHistoryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INVOICES_FIELD_NUMBER: builtins.int

    @property
    def invoices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InvoiceSummary]:
        ...

    def __init__(self, *, invoices: collections.abc.Iterable[global___InvoiceSummary] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['invoices', b'invoices']) -> None:
        ...
global___GetInvoiceHistoryResponse = GetInvoiceHistoryResponse

@typing_extensions.final
class GetItemizedInvoiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___GetItemizedInvoiceRequest = GetItemizedInvoiceRequest

@typing_extensions.final
class GetItemizedInvoiceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INVOICE_FIELD_NUMBER: builtins.int

    @property
    def invoice(self) -> global___Invoice:
        ...

    def __init__(self, *, invoice: global___Invoice | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['invoice', b'invoice']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['invoice', b'invoice']) -> None:
        ...
global___GetItemizedInvoiceResponse = GetItemizedInvoiceResponse

@typing_extensions.final
class GetBillingSummaryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str

    def __init__(self, *, org_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['org_id', b'org_id']) -> None:
        ...
global___GetBillingSummaryRequest = GetBillingSummaryRequest

@typing_extensions.final
class GetBillingSummaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USAGE_SUMMARY_FIELD_NUMBER: builtins.int
    INVOICES_FIELD_NUMBER: builtins.int
    STATEMENT_BALANCE_FIELD_NUMBER: builtins.int
    CURRENT_BALANCE_FIELD_NUMBER: builtins.int
    CURRENT_MONTH_BALANCE_FIELD_NUMBER: builtins.int
    CURRENT_MONTH_DUE_DATE_FIELD_NUMBER: builtins.int
    INVOICE_EMAIL_FIELD_NUMBER: builtins.int

    @property
    def usage_summary(self) -> global___CurrentMonthUsageSummary:
        ...

    @property
    def invoices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InvoiceSummary]:
        ...
    statement_balance: builtins.float
    'all unpaid balances at the end of the last billing cycle'
    current_balance: builtins.float
    'statement_balance + current_month_usage'
    current_month_balance: builtins.float
    'current_month_usage_cost'

    @property
    def current_month_due_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """due date for current month usage"""
    invoice_email: builtins.str

    def __init__(self, *, usage_summary: global___CurrentMonthUsageSummary | None=..., invoices: collections.abc.Iterable[global___InvoiceSummary] | None=..., statement_balance: builtins.float=..., current_balance: builtins.float=..., current_month_balance: builtins.float=..., current_month_due_date: google.protobuf.timestamp_pb2.Timestamp | None=..., invoice_email: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['current_month_due_date', b'current_month_due_date', 'usage_summary', b'usage_summary']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['current_balance', b'current_balance', 'current_month_balance', b'current_month_balance', 'current_month_due_date', b'current_month_due_date', 'invoice_email', b'invoice_email', 'invoices', b'invoices', 'statement_balance', b'statement_balance', 'usage_summary', b'usage_summary']) -> None:
        ...
global___GetBillingSummaryResponse = GetBillingSummaryResponse