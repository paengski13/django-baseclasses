from .models import PREVIEW_FLAG


class ContentModelAdminMixin(object):
    """Enables staff preview of non-live objects, in combination with
       ContentModelQuerySet.live(request). Note the view must pass a request to
       this method or the preview won't work. """

    def view_on_site(self, obj):
        url = obj.get_absolute_url()
        if not obj.live:
            return url + '?%s=1' % PREVIEW_FLAG
        return url
