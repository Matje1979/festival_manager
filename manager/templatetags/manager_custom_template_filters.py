from django import template
import calendar

register = template.Library()

@register.filter
def month_name_sr(value):
    months_sr = ["Januar", "Februar", "Mart", "April", "Maj", "Jun", "Jul", "Avgust", "Septembar", "Oktobar", "Novembar", "Decembar"]
    return months_sr[value - 1]
   