from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    tools_used = models.TextField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    position= models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    roles = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.position

class PersonalDetail(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    what_i_do = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    contact_address = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname

class Skill(models.Model):
    SKILL_LEVELS = [
        ('BEGINNER', 'BEGINNER'),
        ('INTERMEDIATE', 'INTERMEDIATE'),
        ('EXPERT', 'EXPERT'),
    ]

    name = models.CharField(max_length=255)
    how_good = models.CharField(max_length=13, choices=SKILL_LEVELS, blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    program = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.school

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
