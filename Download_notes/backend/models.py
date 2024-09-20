from django.db import models
import os

# Department Choices
DEPARTMENT_CHOICES = [
    ('BIM', 'BIM'),
    ('BCA', 'BCA'),
    ('CSIT', 'CSIT'),
    ('BHM', 'BHM'),
]

# Folder Category Choices
FOLDER_CHOICES = [
    ('Entrance', 'Entrance'),
    ('Old Question', 'Old Question'),
    ('Prospectus', 'Prospectus'),
    ('Syllabus','Syllabus'),
]

# College or University Choices
COLLEGE_UNIVERSITY_CHOICES = [
    ('College', 'College'),
    ('University', 'University'),
]

# Semester Choices
SEMESTER_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Fifth'),
    ('6', 'Sixth'),
    ('7', 'Seventh'),
    ('8', 'Eighth'),
]

def custom_upload_path(instance, filename):
    """
    Generates the upload path based on the folder category, department, year, semester, and college/university.
    """
    if instance.folder_category == 'Prospectus':
        return os.path.join('uploads', instance.folder_category, filename)
    elif instance.folder_category == 'Old Questions':
        return os.path.join(
            'uploads',
            instance.folder_category,
            instance.department,
            instance.semester,
            instance.year,
            instance.college_or_university,
            filename
        )
    else:
        return os.path.join('uploads', instance.folder_category, instance.department, filename)

class Upload(models.Model):
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)  # Optional for 'Entrance' and 'Prospectus'
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES, blank=True, null=True)  # Optional for 'Entrance' and 'Prospectus'
    folder_category = models.CharField(max_length=100, choices=FOLDER_CHOICES)
    college_or_university = models.CharField(max_length=100, choices=COLLEGE_UNIVERSITY_CHOICES, blank=True, null=True)  # Optional for 'Old Questions'
    pdf_file = models.FileField(upload_to=custom_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.folder_category} - {self.department} - {self.year or 'N/A'} - {self.semester or 'N/A'} - {self.college_or_university or 'N/A'}"
