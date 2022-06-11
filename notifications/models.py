from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class TblUserFirebase(models.Model):
    id = models.AutoField(primary_key=True, db_column="fld_ai_id")
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_id")
    firebase_id = models.CharField(
        max_length=255, blank=True, null=True, default="NA", db_column="fld_firebase_id")
    is_send_push = models.BooleanField(
        default=True, db_column="fld_is_send_push")
    device_info = models.TextField(default="NA", db_column="fld_device_info")
    is_active = models.BooleanField(default=True, db_column="fld_is_active")
    is_delete = models.BooleanField(default=False, db_column="fld_is_delete")
    created_datetime = models.DateTimeField(
        auto_now_add=True, db_column="fld_created_datetime")

    def __str__(self) -> str:
        return f'{self.user_id.email} on {str(self.created_datetime)}'

    class Meta:
        managed = True
        db_table = 'tbl_user_firebase'


class TblNotificationConfig(models.Model):
    NOTIFICATIONS_TYPE_CHOICE = (
        ('forgets to check-in', 'forgets to check-in'),
        ('offline', 'offline'),
        ('outside of geolocation bound', 'outside of geolocation bound'),
        ('disable tracking', 'disable tracking'),
        ('changes datetime', 'changes datetime'),
    )
    id = models.AutoField(primary_key=True, db_column="fld_ai_id")
    # user_id = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_id")
    notification_type = models.CharField(
        max_length=100, blank=True, null=True, choices=NOTIFICATIONS_TYPE_CHOICE, db_column="fld_notification_type")
    notification_title = models.CharField(
        max_length=255, blank=True, null=True, default="NA", db_column="fld_notification_title")

    notification_body = models.CharField(
        max_length=500, blank=True, null=True, default="NA", db_column="fld_notification_body")

    notification_icon = models.CharField(
        max_length=255, blank=True, null=True, default="NA", db_column="fld_notification_icon")

    is_active = models.BooleanField(default=True, db_column="fld_is_active")
    is_delete = models.BooleanField(default=False, db_column="fld_is_delete")
    created_datetime = models.DateTimeField(
        auto_now_add=True, db_column="fld_created_datetime")

    def __str__(self) -> str:
        return self.notification_type

    class Meta:
        managed = True
        db_table = 'tbl_notification_config'


class TblPushNotificationLog(models.Model):

    id = models.AutoField(primary_key=True, db_column="fld_ai_id")

    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_id")

    notification_type_id = models.ForeignKey(
        TblNotificationConfig, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_notification_type_id")

    user_firebase = models.ForeignKey(
        TblUserFirebase, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_firebase")

    firebase_response = models.TextField(
        blank=True, null=True, default="NA", db_column="fld_firebase_response")

    status_code = models.CharField(
        max_length=10, blank=True, null=True, default="NA", db_column="fld_status_code")

    is_success = models.BooleanField(default=True,  db_column="fld_is_success")

    is_active = models.BooleanField(default=True, db_column="fld_is_active")
    is_delete = models.BooleanField(default=False, db_column="fld_is_delete")
    datetime = models.DateTimeField(
        db_column="fld_datetime")

    created_datetime = models.DateTimeField(
        auto_now_add=True, db_column="fld_created_datetime")

    def __str__(self) -> str:
        return self.user_id.email

    class Meta:
        managed = True
        db_table = 'tbl_push_notification_log'
