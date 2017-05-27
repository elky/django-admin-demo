class RestrictUpdate(object):
    actions = ['delete_selected']

    def save_model(self, request, obj, form, change):
        return

    def save_formset(self, request, form, formset, change):
        formset.save(commit=False)
        return

    def delete_model(self, request, obj):
        return

    def delete_selected(self, request, obj):
        return
