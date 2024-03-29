from django.db import models


    # HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='picture/')
    resume = models.FileField(upload_to='picture/', default='Anupama_Ellath_CV.pdf')

    def __str__(self):
        return self.name
    
    # ABOUT SECTION

class About(models.Model):
    title = models.CharField(max_length=15)
    sub_title= models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='picture/',)

    def __str__(self):
        return self.sub_title
    
    # EXPERIENCE SECTION

class Experience(models.Model):
    title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    period = models.CharField(max_length=30)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
    
    # SKILLS SECTION

class Skills(models.Model):
    title = models.CharField(max_length=50)
    skills = models.TextField(blank=False)
    
    def skillList(self):
        return self.skills.split(',')

    def __str__(self):
        return self.title
    
    # PROJECTS SECTION

class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    skills_used = models.CharField(max_length=100)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self) :
        return self.title
    
    #EDUCATION SECTION

class Education(models.Model):
    title = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    period = models.CharField(max_length=30)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
    
    #CONTACTS SECTION

class Contacts(models.Model):
    contact_links = models.URLField(blank=True)

    def __str__(self):
        return self.contact_links
    