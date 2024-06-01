from django.db import models
def get_model_fields(model: models.Model) -> list:
    return [field.name for field in model._meta.get_fields()]
def get_column_values(column:str, model: models.Model) -> list:
    return list(set(model.objects.values_list(column, flat=True)))
