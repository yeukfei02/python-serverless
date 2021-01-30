from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from datetime import datetime

class NotesModel(Model):
    class Meta:
        table_name = "PythonServerlessNotes"
        region = "ap-southeast-1"
        host = "https://dynamodb.ap-southeast-1.amazonaws.com"
    id = UnicodeAttribute(hash_key=True, null=False)
    content = UnicodeAttribute(null=False)
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())
    updatedAt = UTCDateTimeAttribute(null=False, default=datetime.now())

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(NotesModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))

if not NotesModel.exists():
    NotesModel.create_table(read_capacity_units=1, write_capacity_units=1)