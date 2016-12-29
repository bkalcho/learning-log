from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name_plural = 'entries'

# 18-2. Short Entries: The __str__() method in the Entry model currently
# appends an ellipsis to every instance of Entry when Django shows it in
# the admin site or the shell. Add an if statement to the __str__()
# method that adds an ellipsis only if the entry is more than 50
# characters long. Use the admin site to add an entry that's fewer than
# 50 characters in length, and check that it doesn’t have an ellipsis
# when viewed.

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + '...'