from django.db import models

class Comic(models.Model):
	id = models.IntegerField(primary_key=True, db_column='Id')
	Name = models.CharField(max_length=50)
	Url = models.CharField(max_length=1000)
	ParserConstructor = models.CharField(max_length=200)
	IsActive = models.BooleanField()

	def __unicode__(self):
		return "%s - %s" % (self.Name, self.Url)

	class Meta:
		db_table = u'Comic'

class ComicLog(models.Model):
	id = models.IntegerField(primary_key=True)
	ComicId = models.ForeignKey(Comic, db_column="ComicId")
	ImageUrl = models.CharField(max_length=1000)
	FetchDate = models.DateTimeField()

	def __unicode__(self):
		return "%s - %s" % (self.ImageUrl, self.FetchDate)

	class Meta:
		db_table = u'ComicLog'

class ComicRss(models.Model):
	id = models.IntegerField(primary_key=True)
	ComicLogId = models.ForeignKey(ComicLog, db_column="ComicLogId")

	class Meta:
		db_table = u'ComicRss'
