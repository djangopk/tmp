from django.contrib import admin

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
	fields= ['ids', 'password',]
admin.site.register(Client, ClientAdmin)