from django.db.models import Count
from django.db.models import Q


class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted


def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    
    # initiate a new dict for result
    result = {}

    ''' fetch the statistic from publication:
        using anotate and aggregate feature from django ORM and only fetch needed fields
        for better query performance.
    '''
    statistics = Publication.objects\
                            .annotate(total_views=Count('hit', filter=Q(hit__action=Hit.PAGEVIEW)))\
                            .annotate(total_downloads=Count('hit', filter=Q(hit__action=Hit.DOWNLOAD)))\
                            .distinct('journal').values('journal_id, total_views', 'total_downloads')
    
    # loop the statistic and contruct the dict result
    for statistic in statistics:
        result[statistic['journal_id']] = (statistic['total_views'], statistic['total_downloads'])
    return result
