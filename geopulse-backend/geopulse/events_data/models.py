from django.db import models

class GeoFlashpointRisk(models.Model):
    EVENT_ID = models.BigIntegerField(primary_key=True)
    EVENT_YYYYMMDD = models.DateField()
    EVENT_YYYYMM = models.IntegerField()
    EVENT_YYYY = models.IntegerField()
    EVENT_YYYYFFFF = models.FloatField()
    INITIATOR_CODE = models.CharField(max_length=10)
    INITIATOR_NAME = models.CharField(max_length=255)
    INITIATOR_COUNTRY_CODE = models.CharField(max_length=10)
    INITIATOR_KNOWN_GROUP_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_ETHNIC_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_RELIGION1_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_RELIGION2_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_TYPE1_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_TYPE2_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_TYPE3_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_CODE = models.CharField(max_length=10)
    TARGET_NAME = models.CharField(max_length=255)
    TARGET_COUNTRY_CODE = models.CharField(max_length=10)
    TARGET_KNOWN_GROUP_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_ETHNIC_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_RELIGION1_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_RELIGION2_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_TYPE_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_TYPE2_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_TYPE3_CODE = models.CharField(max_length=10, null=True, blank=True)
    IS_EVENT_ORIGIN = models.BooleanField()
    EVENT_CODE = models.CharField(max_length=10)
    EVENT_BASE_CODE = models.CharField(max_length=10)
    EVENT_ORIGIN_CODE = models.CharField(max_length=10)
    EVENT_CLASSIFICATION = models.IntegerField()  # Verbal Cooperation (1), Material Cooperation (2), Verbal Conflict (3), Material Conflict (4)
    STABILITY_SCALE = models.FloatField()  # Goldstein Scale
    EVENT_MENTION_COUNT = models.IntegerField()
    EVENT_MENTION_SOURCES_COUNT_LAST15MINUTES = models.IntegerField(null=True, blank=True)
    EVENT_MENTION_ARTICLES_COUNT_LAST15MINUTES = models.IntegerField(null=True, blank=True)
    EVENT_AVG_TONE_SOURCES_LAST15MINUTES = models.FloatField()  # -100 (extremely negative) to +100 (extremely positive), commonly -10 to +10, 0 being neutral
    INITIATOR_GEO_TYPE = models.IntegerField()  # Country (1), US State (2), US City (3), World City (int'l city) (4), World state (int'l state) (5)
    INITIATOR_GEO_FULLNAME = models.CharField(max_length=255)
    INITIATOR_GEO_COUNTRY_CODE = models.CharField(max_length=10)
    INITIATOR_GEO_ADM1_CODE = models.CharField(max_length=10)
    INITIATOR_GEO_ADM2_CODE = models.CharField(max_length=10, null=True, blank=True)
    INITIATOR_GEO_LATITUDE = models.FloatField()
    INITIATOR_GEO_LONGITUDE = models.FloatField()
    INITIATOR_GEO_FEATURE_ID = models.CharField(max_length=20)
    TARGET_GEO_TYPE = models.IntegerField()
    TARGET_GEO_FULLNAME = models.CharField(max_length=255)
    TARGET_GEO_COUNTRY_CODE = models.CharField(max_length=10)
    TARGET_GEO_ADM1_CODE = models.CharField(max_length=10)
    TARGET_GEO_ADM2_CODE = models.CharField(max_length=10, null=True, blank=True)
    TARGET_GEO_LATITUDE = models.FloatField()
    TARGET_GEO_LONGITUDE = models.FloatField()
    TARGET_GEO_FEATURE_ID = models.CharField(max_length=20)
    FLASHPOINT_GEO_TYPE = models.IntegerField()
    FLASHPOINT_GEO_FULLNAME = models.CharField(max_length=255)
    FLASHPOINT_GEO_COUNTRY_CODE = models.CharField(max_length=10)
    FLASHPOINT_GEO_ADM1_CODE = models.CharField(max_length=10)
    FLASHPOINT_GEO_ADM2_CODE = models.CharField(max_length=10, null=True, blank=True)
    FLASHPOINT_GEO_LATITUDE = models.FloatField()
    FLASHPOINT_GEO_LONGITUDE = models.FloatField()
    FLASHPOINT_GEO_FEATURE_ID = models.CharField(max_length=20)
    DATEADDED = models.DateField()
    SOURCEURL = models.TextField()
    class Meta:
        indexes = [
            models.Index(fields=['EVENT_YYYYMMDD']),
            models.Index(fields=['EVENT_YYYYMM']),
            models.Index(fields=['EVENT_YYYY']),
            models.Index(fields=['INITIATOR_CODE']),
            models.Index(fields=['TARGET_CODE']),
            models.Index(fields=['INITIATOR_COUNTRY_CODE']),
            models.Index(fields=['TARGET_COUNTRY_CODE']),
            models.Index(fields=['EVENT_CODE']),
            models.Index(fields=['INITIATOR_GEO_LATITUDE', 'INITIATOR_GEO_LONGITUDE']),
            models.Index(fields=['TARGET_GEO_LATITUDE', 'TARGET_GEO_LONGITUDE']),
            models.Index(fields=['FLASHPOINT_GEO_LATITUDE', 'FLASHPOINT_GEO_LONGITUDE']),
    ]
    def __str__(self):
        return f"{self.EVENT_ID} - {self.INITIATOR_NAME} vs {self.TARGET_NAME}"

