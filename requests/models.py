from django.db import models


class CustomServiceRequest(models.Model):
    """
    Stores custom service requests submitted by users.
    """

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_QUOTED = 'quoted'
    STATUS_CONVERTED = 'converted'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_QUOTED, 'Quoted'),
        (STATUS_CONVERTED, 'Converted'),
        (STATUS_CLOSED, 'Closed'),
    ]

    TYPE_CUSTOM = 'custom'
    TYPE_RESTORATION = 'restoration'
    TYPE_ENGRAVING = 'engraving'
    TYPE_OTHER = 'other'

    REQUEST_TYPE_CHOICES = [
        (TYPE_CUSTOM, 'Custom Service'),
        (TYPE_RESTORATION, 'Restoration'),
        (TYPE_ENGRAVING, 'Engraving'),
        (TYPE_OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    request_type = models.CharField(
        max_length=30,
        choices=REQUEST_TYPE_CHOICES,
        default=TYPE_CUSTOM,
    )

    description = models.TextField()

    budget = models.CharField(max_length=50, blank=True)
    preferred_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_request_type_display()}"
