from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = 'mail.thread'
    _description = "My demo model"

    
    name = fields.Char(compute='_make_name', store=True)
    customer = fields.Many2one('res.partner', required=True)
    done_date = fields.Date()
    salesperson = fields.Many2one('res.users')
    state = fields.Selection([('planned',"Planned"),('done',"Done"),('cancelled',"Cancelled")], default='planned')
    lead_id = fields.Many2one('crm.lead', ondelete='cascade', string="Lead", required=True)
    
    @api.depends('customer')
    def _make_name(self):
        for r in self:
            r.name = f"Demo {r.id:02}"

    def planned_progressbar(self):
        self.write({
        'state': 'planned'
        })

    def cancelled_progressbar(self):
        self.write({
        'state': 'cancelled'
        })

    def done_progressbar(self):
        self.write({
        'state': 'done',
        })


class Lead(models.Model):
    _inherit = 'crm.lead'

    demo_ids = fields.One2many('demo.demo', 'lead_id')
    demo_count = fields.Integer(compute='_demo_count')

    @api.depends('demo_ids')
    def _demo_count(self):
        for r in self:
            r.demo_count = len(r.demo_ids)

    def demo_new(self):
        return {
            'name': 'New demo',
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'context': {
                'default_lead_id':self.id,
                'default_customer':self.partner_id.id,
                'default_salesperson':self.env.user.id,
            },
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("my_demo.demo_form_view").id,
            'target': 'new'
        }

    def demo_all(self):
        view_id = self.env.ref("my_demo.demo_tree_view").id
        return {
            'name': f'Demos for {self.name}',
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'views': [[view_id,'tree']],
            'domain': [('lead_id','=',self.id)],
            'target': 'current',
        }
    
