# arvestust:audit
from auditlog.registry import auditlog
from ..models import Activity
from ..models import Comment
from ..models import File
from ..models import Image
from ..models import Tag

auditlog.register(Activity)
auditlog.register(Comment)
auditlog.register(File)
auditlog.register(Image)
auditlog.register(Tag)
