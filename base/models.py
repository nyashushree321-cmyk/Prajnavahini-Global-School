from django.db import models


class OrderedActiveModel(models.Model):
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['order', 'id']


class LeaderMessage(OrderedActiveModel):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='leaders/')
    bio = models.TextField(help_text="One paragraph per line; each line is rendered as its own <p>.")

    def __str__(self):
        return self.name


class Mentor(OrderedActiveModel):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='mentors/')
    quote = models.TextField()

    def __str__(self):
        return self.name


class InfraFeature(OrderedActiveModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='infra/')
    description = models.TextField()
    background_color = models.CharField(
        max_length=20, default='#021341',
        help_text="CSS color used for the card background, matches the original design's alternating colors.",
    )

    def __str__(self):
        return self.title


class AfterSchoolProgram(OrderedActiveModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='after_school/')

    def __str__(self):
        return self.title


class CampusFacility(OrderedActiveModel):
    image = models.ImageField(upload_to='facilities/')
    caption = models.CharField(max_length=300)

    def __str__(self):
        return self.caption


class CurricularProgram(OrderedActiveModel):
    image = models.ImageField(upload_to='curricular/')
    age_badge = models.CharField(max_length=50, help_text="e.g. 'Age 3+'")
    title = models.CharField(max_length=200)
    features = models.TextField(help_text="One bullet point per line.")

    def __str__(self):
        return self.title


class OngoingClass(OrderedActiveModel):
    image = models.ImageField(upload_to='classes/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class BlogPost(OrderedActiveModel):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog/')
    excerpt = models.TextField()
    author = models.CharField(max_length=100, default='Admin')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQItem(OrderedActiveModel):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question


class ContactMessage(models.Model):
    SOURCE_CHOICES = [
        ('about', 'About Page'),
        ('contact', 'Contact Page'),
        ('faq', 'FAQ Page'),
    ]
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField(blank=True)
    source_page = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='contact')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d})"


class Application(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Application Details
    classApplied = models.CharField('Class Applied For', max_length=100)
    year = models.CharField('Year', max_length=20)
    academicYear = models.CharField('Academic Year', max_length=20)

    # Personal Details
    studentName = models.CharField('Student Name', max_length=200)
    gender = models.CharField('Gender', max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField('Date of Birth')
    bloodGroup = models.CharField('Blood Group', max_length=10, blank=True)
    motherTongue = models.CharField('Mother Tongue', max_length=100, blank=True)
    birthPlace = models.CharField('Birth Place', max_length=150, blank=True)
    nationality = models.CharField('Nationality', max_length=100, blank=True)
    aadhaar = models.CharField('Aadhaar Number', max_length=20, blank=True)

    # Parent Details
    fatherName = models.CharField('Father Name', max_length=200)
    motherName = models.CharField('Mother Name', max_length=200)
    fatherMobile = models.CharField('Father Mobile', max_length=20)
    motherMobile = models.CharField('Mother Mobile', max_length=20)

    # Address
    address = models.TextField('Address')

    agree = models.BooleanField('Agreed to Terms', default=False)
    confirmed = models.BooleanField('Final Submit Confirmed', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.studentName} - {self.classApplied}"
