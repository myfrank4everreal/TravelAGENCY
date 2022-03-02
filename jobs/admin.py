from django.contrib import admin
from .models import EducationalLevel, Jobs, \
    JobCategory,\
        JobAdmin, \
            EmploymentType, \
                CareerLevel, \
                    MonthlySalary, \
                        EducationalLevel, \
                            City






admin.site.register(City)
admin.site.register(Jobs)
admin.site.register(JobCategory)
admin.site.register(JobAdmin)
admin.site.register(EmploymentType)
admin.site.register(CareerLevel)
admin.site.register(MonthlySalary)
admin.site.register(EducationalLevel)

