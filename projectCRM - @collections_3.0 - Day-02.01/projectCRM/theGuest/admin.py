from django.contrib import admin
from .models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager
admin.site.register(RecruitDeveloper)
admin.site.register(RecruitHr)
admin.site.register(RecruitDeveloperAsProjectManager)
admin.site.register(WorksOnLanguage)
