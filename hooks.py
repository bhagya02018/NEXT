# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hire_purchase"
app_title = "Hire Purchase"
app_publisher = "Korecent Solutions Pvt Ltd"
app_description = "Hire Purchase ERPNext Module"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kartik@korecent.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hire_purchase/css/hire_purchase.css"
app_include_js = [
    "/assets/hire_purchase/js/transaction.js",
    "/assets/hire_purchase/js/guarantors_quick_entry.js"
]
# include js, css files in header of web template
# web_include_css = "/assets/hire_purchase/css/hire_purchase.css"
# web_include_js = "/assets/hire_purchase/js/hire_purchase.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hire_purchase.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hire_purchase.install.before_install"
# after_install = "hire_purchase.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hire_purchase.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Customer": {
        "validate": "hire_purchase.utils.validate_customer"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hire_purchase.tasks.all"
# 	],
# 	"daily": [
# 		"hire_purchase.tasks.daily"
# 	],
# 	"hourly": [
# 		"hire_purchase.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hire_purchase.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hire_purchase.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hire_purchase.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hire_purchase.event.get_events"
# }

fixtures = [
    {
        "doctype": "Custom Script",
        "filters": {
            "dt": [
                "in", ["Customer", "Sales Invoice", "Item"]
            ]
        }
    },
    {
        "doctype": "Custom Field",
        "filters": {
            "dt": [
                "in", ["Customer", "Sales Invoice", "Item"]
            ]
        }
    }
]
