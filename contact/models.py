from django.db import models


class ContactMessage(models.Model):
    """
    Stores general enquiries submitted via the contact form.
    """
    STATUS_NEW = 'new'
    STATUS_REPLIED = 'replied'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_REPLIED, 'Replied'),
        (STATUS_ARCHIVED, 'Archived'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        subject = self.subject.strip() or "No Subject"
        return f"Message from {self.name} <{self.email}>: {subject}"
