import frappe

from frappe.utils.response import build_response
from werkzeug.wrappers import Response
import json

@frappe.whitelist(allow_guest=True)
def get_manifest():
    """Returns the web manifest settings for the PWA application"""
    return Response(
        response=frappe.get_doc("PWA Settings").webmanifest,
        content_type="application/json"
    )

@frappe.whitelist(allow_guest=True)
def get_assetlinks():
    """Returns the assetlinks for the PWA application"""
    return Response(
        response=frappe.get_doc("PWA Settings").assetlinks,
        content_type="application/json"
    )