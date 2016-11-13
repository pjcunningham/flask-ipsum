# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import InputRequired, ValidationError


RESOURCE_ERROR_MESSAGE = 'Invalid resource name'
COUNT_ERROR_MESSAGE = 'Count must be an integer value between 1 and 100'
RESPONSE_ERROR_MESSAGE = 'Invalid response output name'


class IpsumV1Form(FlaskForm):

    resource = SelectField(
        'Resource',
        choices=[('api_v1.paragraphs', 'Paragraphs'), ('api_v1.sentences', 'Sentences')],
        render_kw={'title': 'Resource to return'}
    )
    # count = IntegerField('Count', validators=[InputRequired()])
    count = SelectField(
        'Count',
        choices=[(i, str(i)) for i in [5, 10, 25, 75, 100]],
        coerce=int,
        render_kw={'title': 'Quantity of resources to return'}
    )
    response_format = SelectField(
        'Output',
        choices=[('html', 'Html (literal)'), ('html_code', 'Html (markup)'), ('json', 'JSON'), ('text', 'Text')],
        render_kw={'title': 'Output format'}
    )

    def validate_resource(form, field):

        if field.data not in ['api_v1.paragraphs', 'api_v1.sentences']:
            raise ValidationError(RESOURCE_ERROR_MESSAGE)

    def validate_count(form, field):

        try:
            _ = int(field.data)
        except:
            raise ValidationError(COUNT_ERROR_MESSAGE)

        if (field.data < 1) or (field.data > 100) :
            raise ValidationError(COUNT_ERROR_MESSAGE)

    def validate_response_format(form, field):

        if field.data not in ['html', 'html_code', 'json', 'text']:
            raise ValidationError(RESPONSE_ERROR_MESSAGE)
