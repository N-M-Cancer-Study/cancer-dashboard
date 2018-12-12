from django.conf import settings

from edc_model_wrapper import ModelWrapper


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'cancer_subject.subjectconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('subject_dashboard_url')
    next_url_attrs = ['subject_identifier']
    querystring_attrs = [
        'screening_identifier', 'first_name', 'initials', 'modified']
