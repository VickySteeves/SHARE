from django.db import models
from django.db import IntegrityError
from django.contrib.postgres.fields import JSONField

from share.models.base import ShareObject
from share.models.fields import ShareForeignKey, URIField, ShareURLField, ShareManyToManyField
from share.apps import ShareConfig as share_config


__all__ = ('Venue', 'Award', 'Tag', 'Link', 'Subject', 'SubjectSynonym')

# TODO Rename this file


class Venue(ShareObject):
    name = models.TextField(blank=True)
    venue_type = ShareURLField(blank=True)
    location = ShareURLField(blank=True)
    community_identifier = ShareURLField(blank=True)

    def __str__(self):
        return self.name


class Award(ShareObject):
    # ScholarlyArticle has an award object
    # it's just a text field, I assume our 'description' covers it.
    award = ShareURLField(blank=True)
    description = models.TextField(blank=True)
    url = ShareURLField(blank=True)
    entities = ShareManyToManyField('Entity', through='ThroughAwardEntities')

    def __str__(self):
        return self.description


class Tag(ShareObject):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Link(ShareObject):
    url = URIField(db_index=True)
    type = models.TextField(choices=share_config.link_type_choices)

    def __str__(self):
        return self.url


class Subject(models.Model):
    lineages = JSONField(editable=False)
    parents = models.ManyToManyField('self')
    name = models.TextField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self):
        raise IntegrityError('Subjects are an immutable set! Do it in bulk, if you must.')


class SubjectSynonym(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='synonyms')
    synonym = models.TextField(db_index=True)

    def __str__(self):
        return self.synonym

    def save(self):
        raise IntegrityError('Subjects synonyms are an immutable set! Do it in bulk, if you must.')

    class Meta:
        unique_together = ('subject', 'synonym')


# Through Tables for all the things

class ThroughLinks(ShareObject):
    link = ShareForeignKey(Link)
    creative_work = ShareForeignKey('AbstractCreativeWork')

    class Meta:
        unique_together = ('link', 'creative_work')


class ThroughVenues(ShareObject):
    venue = ShareForeignKey(Venue)
    creative_work = ShareForeignKey('AbstractCreativeWork')

    class Meta:
        unique_together = ('venue', 'creative_work')


class ThroughAwards(ShareObject):
    award = ShareForeignKey(Award)
    creative_work = ShareForeignKey('AbstractCreativeWork')

    class Meta:
        unique_together = ('award', 'creative_work')


class ThroughTags(ShareObject):
    tag = ShareForeignKey(Tag)
    creative_work = ShareForeignKey('AbstractCreativeWork')

    class Meta:
        unique_together = ('tag', 'creative_work')


class ThroughAwardEntities(ShareObject):
    award = ShareForeignKey('Award')
    entity = ShareForeignKey('Entity')

    class Meta:
        unique_together = ('award', 'entity')


class ThroughSubjects(ShareObject):
    subject = models.ForeignKey('Subject')
    creative_work = ShareForeignKey('AbstractCreativeWork')

    class Meta:
        unique_together = ('subject', 'creative_work')
