from rest_framework import serializers
from .models import Customer,Book
from datetime import datetime

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    dias_em_atraso = serializers.SerializerMethodField('dias_em_atraso_m')
    multa = serializers.SerializerMethodField('multa_m')
    juros_ao_dia = serializers.SerializerMethodField('juros_ao_dia_m')
    status_desc = serializers.SerializerMethodField('status_desc_m')
    cliente_desc = serializers.SerializerMethodField('cliente_desc_m')

    def dias_em_atraso_m(self, obj):
        if obj.reservation_date is not None:
            today = datetime.now().replace(tzinfo=None)
            diff = today - obj.reservation_date.replace(tzinfo=None) # seconds
            days = diff / 60 / 60 / 24
            # 3 dias = 60 * 60 * 24 * 3
            return days.days
        else:
            return "Livro disponivel"
    def multa_m(self, obj):
        if obj.reservation_date is not None:
            today = datetime.now().replace(tzinfo=None)
            diff = today - obj.reservation_date.replace(tzinfo=None) # seconds
            daysDiff = diff / 60 / 60 / 24
            days = daysDiff.days
        
            if ( days < 3 ):
                return "3%"
            elif days >= 3 and days < 5:
                return "5%"
            elif days >= 5:
                return "7%"
            else:
                return "0%"
        else:
            return "Livro disponivel"
    def juros_ao_dia_m(self, obj):
        if obj.reservation_date is not None:
            today = datetime.now().replace(tzinfo=None)
            diff = today - obj.reservation_date.replace(tzinfo=None) # seconds
            daysDiff = diff / 60 / 60 / 24
            days = daysDiff.days
        
            if ( days < 3 ):
                return "0.2%"
            elif days >= 3 and days < 5:
                return "0.4%"
            elif days >= 5:
                return "0.6%"
            else:
                return "0%"
        else:
            return "Livro disponivel"

    def status_desc_m(self, obj):
        if obj.status == 0:
            return "Emprestado"
        else:
            return "Disponivel"
    def cliente_desc_m(self, obj):
        if obj.customer is not None:
            return obj.customer.name
        else:
            return ""

    class Meta:
        model=Book
        fields=('id', 'title', 'status_desc', 'cliente_desc', 'reservation_date', 'dias_em_atraso', 'multa', 'juros_ao_dia')
