from odoo import models, fields


class JobPosition(models.Model):

    _name = 'job.positions'
    _rec_name = 'job_positions'
    _inherit = ['mail.thread']

    job_positions = fields.Char(string='Job Positions')


class OrganisationType(models.Model):
    _name = 'organisation.types'
    _rec_name = 'organisation_type'

    organisation_type = fields.Char(string='Organisation Type')


class CredentialTrustSetup(models.Model):
    _name = 'credential.setup'
    _rec_name = 'credential_trust_setup'

    credential_trust_setup = fields.Char(string='CeCredential Trust Setup')


class JobFunctions(models.Model):

    _inherit = 'res.partner'

    # external = fields.Char(string='Internal Name')
    job_function = fields.Many2many('job.positions', string='Roles')
    credentials_setup = fields.Many2one('credential.setup', string='CeCredential Trust Setup')
    organisation_type = fields.Many2one('organisation.types', string='Organisation Type')

    organization_no = fields.Integer(string="Organization No")
    products = fields.Many2many('product.product', string="Organisation Products")
    services = fields.Many2many('product.product', string="Organisation Services")
    account_owner = fields.Many2one('res.partner', string="Account Owner")
    notes = fields.Text(string="Notes")

    # first_name = fields.Char(string="First Name")
    # last_name = fields.Char(string="Last name")
    organisation_name = fields.Many2one('res.company', string="Organisation Name")
    primary = fields.Boolean(string="Primary")
    extension = fields.Integer(string="Extension")
    fax = fields.Integer(string="Fax")
    contact_owner = fields.Many2one('res.partner', string="Contact Owner")
    reports_to = fields.Many2one('res.partner', string="Reports To")
    department = fields.Many2one('hr.department', string="Department")
    last_stay_date = fields.Date(string="Last Stay In Touch Date")
    contact_street = fields.Char(string="Contact Street")
    contact_city = fields.Char(string="Contact City")
    contact_province = fields.Many2one('res.country.state', string="Contact State/Province")
    contact_zip = fields.Char(string="Contact Zip/Postal Code")
    contact_country = fields.Many2one('res.country', string="Contact Country")


class StockPicker(models.Model):
    _inherit = 'stock.picking'

    external = fields.Char(string='Internal Name')
