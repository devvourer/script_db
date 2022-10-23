from django.db import models


class Contact(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=11, null=True)
    name = models.CharField(verbose_name='Имя', max_length=50, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, null=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, null=True)


# class Pochta(models.Model):
    # rpobarcode_ccode
    # mailtype_ncode
    # mailtypegroup_ccode
    # mailctg_ncode
    # gr_weight
    # rpo_sndr_name
    # rpo_inn_ccode
    # rpo_kpp_ccode
    # sndr_acnt_ccode
    # index_to_ccode
    # index_ufps_to_ccode
    # settlement_to_name
    # macroregion_to_ncode
    # rpo_rcpn_name
    # rpo_rcpn_phone_ccode
    # assigned_in_private_office_flag
    # customs_notice_flag
    # accept_local_dts
    # accept_local_timezone
    # index_accept_ccode
    # postobjecttype_accept_ccode
    # accept_cutoff_local_time
    # accept_with_cutoff_local_dts
    # index_border_firstmile_exit_ccode
    # index_ufps_accept_ccode
    # settlement_accept_name
    # macroregion_accept_ncode
    # postobjecttype_firstmile_exit_ccode
    # firstmile_exit_local_dts
    # firstmile_exit_local_timezone
    # firstmile_cutoff_local_time
    # firstmile_deadline_local_dts
    # index_border_potencialdelivery_ccode
    # postobjecttype_potencialdelivery_ccode
    # firstoper_in_potencialdelivery_local_dts
    # firstoper_in_potencialdelivery_local_timezone
    # arrival_local_dts
    # arrival_local_timezone
    # transferred_to_PVZ_local_dts
    # transferred_to_PVZ_local_timezone
    # first_delivery_attempt_local_dts
    # first_delivery_attempt_local_timezone
    # operattr_first_delivery_attempt_ncode
    # delivery_local_dts
    # delivery_local_timezone
    # index_delivery_ccode
    # opertype_delivery_ncode
    # operattr_delivery_ncode
    # return_local_dts
    # return_local_timezone
    # operattr_return_ncode
    # opertype_return_ncode
    # delivery_term_days
    # general_deadline_local_dts
    # arrive_cutoff_local_time
    # lastmile_deadline_local_dts 
    # lastrpo_local_dts 
    # lastrpo_local_timezone
    # operattr_lastrpo_ncode 
    # opertype_lastrpo_ncode
    # index_lastrpo_ccode  
    # real_term_calendar_days    
    # real_term_working_days     
    # waystatus_ccode   
    # generalstatus_ccode 
    # internalstatus_ccode 
    # clientstatus_ccode  
    # resending_local_dts 
    # resending_local_timezone 
    # editing_local_dts   
    # editing_local_timezone
    # value_date
    # dws_job  
    # deleted_flag 
    # as_of_date


    
class CsvData(models.Model):
    file = models.FileField()
