from django.contrib import admin

import app

admin.site.register(app.models.Author)
admin.site.register(app.models.Book)
admin.site.register(app.models.Review)