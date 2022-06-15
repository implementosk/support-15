# -*- coding: utf-8 -*-

from odoo import api, Command, fields, models, tools, _

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    rel_task_id = fields.Many2one('project.task', string=_("Related Task"))

    def create_new_task(self):
        self.ensure_one()
        wizard = self.env['helpdesk.task.wizard'].create({
            'ticket_id': self.id,
        })
        return wizard.get_action()


class HelpdeskTaskWizard(models.TransientModel):
    _name = 'helpdesk.task.wizard'

    project_id = fields.Many2one('project.project')
    ticket_id = fields.Many2one('helpdesk.ticket')


    def get_action(self):
        self.ensure_one()
        return {
            'name': _('Create new Task from this Ticket'),
            'type': 'ir.actions.act_window',
            'res_model': 'helpdesk.task.wizard',
            'res_id': self.id,
            'view_mode': 'form',
            'views': [(False, 'form')],
            'target': 'new',
            'context': self.env.context,
        }

    def action_done(self):
        self.ensure_one()
        task = self.env['project.task'].create(self._prepare_task_vals(self.project_id))
        self.ticket_id.rel_task_id = task.id


    def _prepare_task_vals(self, project_id):
        self.ensure_one()
        return {
            'project_id': project_id.id,
            'description': self.ticket_id.description,
            'name': self.ticket_id.name,
        }
