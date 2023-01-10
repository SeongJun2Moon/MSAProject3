from sqlalchemy import Column, TIMESTAMP as Timestamp, text, String


class TimestampMixin(object):
    user_id = Column(String(20), primary_key=True)
    create_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp'))
    updated_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp on update current_timestamp'))