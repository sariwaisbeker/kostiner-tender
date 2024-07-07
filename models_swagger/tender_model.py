from flask_restx import Namespace, fields, namespace

namespace_tender = Namespace(name=str('tender'),
                      description='tenders',
                      path='/api',
                      ordered=True
                      )

participant_model = namespace_tender.model('Participant', {
    'name': fields.String(required=True, description='Participant name'),
    'amount': fields.Float(required=True, description='Amount'),
    'isWinner': fields.Boolean(required=True, description='Did he win')
})

disqualified_participants_model = namespace_tender.model('disqualified_participants',{
    'name': fields.String(required=True, description='disqualified_participants name'),
    'reason': fields.String(required=True, description='the reason for disqualification')
})

details_model = namespace_tender.model('Details', {
    'participants': fields.List(fields.Nested(participant_model), required=True, description='List of participants'),
    'disqualified_participants': fields.List(fields.Nested(disqualified_participants_model), required=True, description='Participants who do not fit the tender rules and are disqualified'),
    'committee_member': fields.String(required=True, description='committee_member'),

})

path_model = namespace_tender.model('Path', {
    'csv_file_path': fields.String(required=True, description='Path to the uploaded CSV file')
})

# Define the main model
tender_model = namespace_tender.model('Tender', {
    'tender_id': fields.String(required=True, description='Tender ID'),
    'category': fields.String(required=True, description='Category of trender'),
    'tender_name': fields.String(required=True, description='Name of trender'),
    'date': fields.Date(required=True, description='date of trender'),
    'details': fields.Nested(details_model, required=True, description='Details object'),
    'csv_file_path': fields.String(required=True, description='Path to the uploaded CSV file')
})