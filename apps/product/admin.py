from django.contrib import admin
from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        if str(model) == "<class 'rest_framework.authtoken.models.Token'>":
            continue
        model_class_name = f"mymodel{model}"
        # all_fields = model._meta.get_fields()
        all_fields = model._meta.fields
        model_field_names = [f.name for f in all_fields]
        class model_class_name(admin.ModelAdmin):
            list_display = model_field_names

        admin.site.register(model, model_class_name)
    except:
        pass
        # print(f"{model} registration fail")



