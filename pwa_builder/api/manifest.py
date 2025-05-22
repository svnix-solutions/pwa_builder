import frappe
import json
from frappe.utils.response import build_response


@frappe.whitelist(allow_guest=True)
def get_manifest():
    """Returns the web manifest settings for the PWA application"""
    pwa_settings = frappe.get_doc("PWA Settings")
    webmanifest = json.loads(pwa_settings.webmanifest)
    
    for key, value in webmanifest.items():
        setattr(frappe.response, key, value)

    return build_response("json")