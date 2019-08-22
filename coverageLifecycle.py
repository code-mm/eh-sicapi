from .api import http_method

coverage_lifecycle_endpoint = {
    'request_quote': 'coverage',
    'update_quote': 'coverage/{}',              # cover-id
    'activate_cover': 'coverage/{}/activate',   # cover-id
    'reject_cover': 'coverage/{}/reject',       # id
    'settle_cover': 'coverage/{}/settle',       # id
    'claim_cover': 'coverage/{}/claim',         # cover-id
    'get-claim': 'coverage/{}/claim'            # cover-id
}

class CoverageLifecycle:
    def __init__(self, api):
        self.api = api

    def request_quote(self, seller_id, buyer_id, invoice_amount, invoice_currency, invoice_due_at, invoice_issued_at, invoice_number, invoice=None):
        raise NotImplementedError

    def activate_cover(self, cover_id):
        raise NotImplementedError

    def reject_cover(self, id):
        raise NotImplementedError

    def settle_cover(self, id, settledat):
        raise NotImplementedError

    def claim_cover(self,
            file,
            contacts=None,
            contacts.creditor=None,
            contacts.creditor.contactInformation=None,
            contacts.creditor.contactInformation.firstName=None,
            contacts.creditor.contactInformation.lastName=None,
            contacts.creditor.contactInformation.officePhone=None,
            contacts.creditor.contactInformation.mobilePhone=None,
            contacts.creditor.contactInformation.email=None,
            contacts.debtor=None,
            contacts.debtor.contactInformation=None,
            contacts.debtor.contactInformation.lastName=None,
            contacts.debtor.contactInformation.officePhone=None,
            contacts.debtor.contactInformation.mobilePhone=None,
            contacts.debtor.contactInformation.email=None,
            claimContextInfo=None,
            claimContextInfo.referenceNumber=None,
            claimContextInfo.isInvoiceDisputed=None,
            claimContextInfo.isInsolvencyProceeding=None,
            claimContextInfo.comment=None):
        raise NotImplementedError

    def get_claim(self, cover_id):
        raise NotImplementedError
