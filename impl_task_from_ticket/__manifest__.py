# -*- coding: utf-8 -*-
{
    'name': "Task from Ticket",

    'summary': """
        Addon to assign multiple project tasks to Helpdesk ticket. It differs from standard odoo task linking 
        functionality used for timesheets and purpose of it is to track several tickets for other teams/vendors.
        This addon needs Helpdesk app from enterprise to be installed.""",

    'author': "krnac@implemento.sk",
    'website': "https://implemento.sk",

    'category': 'Uncategorized',
    'version': '15.0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk', 'helpdesk_timesheet', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
    ],
}
