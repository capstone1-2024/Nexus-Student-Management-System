class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    credit_units = Column(Integer)

# More database models...
